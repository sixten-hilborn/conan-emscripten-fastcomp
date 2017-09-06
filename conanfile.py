import os
from conans import ConanFile, CMake
from conans.tools import get, patch


class EmscriptenFastcompConan(ConanFile):
    name = "emscripten-fastcomp"
    version = "1.37.21"
    license = "University of Illinois/NCSA Open Source - https://github.com/kripken/emscripten-fastcomp/blob/master/LICENSE.TXT"
    url = "https://github.com/sixten-hilborn/conan-emscripten-fastcomp"
    settings = {"os": None, "arch": None, "compiler": None, "build_type": ["Release"]}
    exports = ["patch"]
    description = "Recipe for building Emscripten toolchain for cross compilation"
    short_paths = True

    folder = 'emscripten-fastcomp-{0}'.format(version)

    def configure(self):
        pass

    def package_id(self):
        # Don't care which compiler was used when using ems
        self.info.settings.compiler = "any"

    def source(self):
        get('https://github.com/kripken/emscripten-fastcomp/archive/{0}.zip'.format(self.version))

        get('https://github.com/kripken/emscripten-fastcomp-clang/archive/{0}.zip'.format(self.version))
        os.rename('emscripten-fastcomp-clang-{0}'.format(self.version), '{0}/tools/clang'.format(self.folder))


    def build(self):
        patch(patch_file='patch', base_path=self.folder)
        cmake = CMake(self)
        defs = {
            'CMAKE_INSTALL_PREFIX': os.path.join(self.conanfile_directory, 'install'),
            'LLVM_TARGETS_TO_BUILD': 'X86;JSBackend',
            'LLVM_INCLUDE_EXAMPLES': False,
            'LLVM_INCLUDE_TESTS': False,
            'CLANG_INCLUDE_EXAMPLES': False,
            'CLANG_INCLUDE_TESTS': False
        }
        cmake.configure(build_dir='{0}/build'.format(self.folder), source_dir='..', defs=defs)
        cmake.build(target='install')

    def package(self):
        self.copy('*', src='install', dst='.', symlinks=True)

    def package_info(self):
        self.env_info.LLVM = os.path.join(self.package_folder, "bin")

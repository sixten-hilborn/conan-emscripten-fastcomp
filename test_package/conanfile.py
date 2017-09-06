from conans.model.conan_file import ConanFile
import os


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        pass

    def imports(self):
        pass

    def test(self):
        llvm_path = os.environ['LLVM']
        self.run('cd "{0}" && .{1}clang --version'.format(llvm_path, os.sep))

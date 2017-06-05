from conans.model.conan_file import ConanFile
import os


############### CONFIGURE THESE VALUES ##################
default_user = "hilborn"
default_channel = "stable"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    requires = "emscripten-fastcomp/1.37.13@%s/%s" % (username, channel)

    def build(self):
        pass

    def imports(self):
        pass

    def test(self):
        llvm_path = os.environ['LLVM']
        self.run('cd "{0}" && .{1}clang --version'.format(llvm_path, os.sep))

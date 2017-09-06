from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    if platform.system() == "Windows":
        builder.add({'arch': 'x86', 'build_type': 'Release', 'compiler': 'Visual Studio', 'compiler.version': '10'}, {}, {}, {})
        builder.add({'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'Visual Studio', 'compiler.version': '10'}, {}, {}, {})
    elif platform.system() == "Linux":
        builder.add({'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'gcc', 'compiler.version': '4.9'}, {}, {}, {})
    elif platform.system() == "Darwin":
        builder.add({'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang', 'compiler.version': '8.1'}, {}, {}, {})

    builder.run()


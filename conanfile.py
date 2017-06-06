from conans import ConanFile, tools
import os

class HelloConan(ConanFile):
    name = 'Hello'
    version = '1.0'
    license = 'MIT'
    url = ''
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'myproj description'
    exports_sources = "src/*"
    generators = "scons"

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        os.makedirs("build")
        # FIXME: Compiler, version, arch are hardcoded, not parametrized
        with tools.chdir("build"):
            self.run('scons -C {}/src {}'.format(self.source_folder, debug_opt))
        
    def package(self):
        self.copy("*.h", "include", src="src")
        self.copy("*.lib", "lib", keep_path=False)
        self.copy("*.a", "lib", keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = ["hello"]

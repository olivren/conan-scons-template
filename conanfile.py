from conans import ConanFile, tools
import os

class HelloConan(ConanFile):
    
    # Attributes of the Hello library, that you should specify in any case
    name = 'Hello'
    version = '1.0'
    license = 'MIT'
    url = ''
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'Hello lib description'
    
    # All the code below this comment is an example of how you can compile the
    # Hello library itself using the SCons build tool. If the library you want to
    # package is not based on SCons, just delete everything under this comment
    # and also the content of the directory `src`.
    
    # Use this attribute only if the source code of the Hello library is not
    # external, and lives next to the recipe.
    exports_sources = 'src/*'
    
    # This is useful only if the Hello library has dependencies on other Conan
    # packages.
    generators = 'scons'

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        os.makedirs('build')
        # FIXME: Compiler, version, arch are hardcoded, not parameterized
        with tools.chdir('build'):
            self.run('scons -C {}/src {}'.format(self.source_folder, debug_opt))
        
    def package(self):
        self.copy('*.h', 'include', src='src')
        self.copy('*.lib', 'lib', keep_path=False)
        self.copy('*.a', 'lib', keep_path=False)
        
    def package_info(self):
        self.cpp_info.libs = ['hello']

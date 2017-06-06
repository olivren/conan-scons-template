from conans import ConanFile
import os

class HelloTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    requires = 'Hello/1.0@user/stable'
    generators = 'scons'

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        self.run('scons -C {} {}'.format(self.conanfile_directory, debug_opt))

    def test(self):
        self.run(os.path.join('.', 'example'))

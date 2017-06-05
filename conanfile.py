from conans import ConanFile, tools

class MyProjConan(ConanFile):
    name = 'myproj'
    version = '1.0'
    license = 'MIT'
    url = 'https://github.com/user/myproj'
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'myproj description'
    
    def source(self):
        pass

    def build(self):
        pass
        
    def package(self):
        pass
        
    def package_info(self):
        pass

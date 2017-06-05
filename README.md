# Conan SCons template

A template for a [Conan package manager][1] recipe, that uses [SCons][2] as its build tool instead of CMake.
It supports MSVC 2017 Pro and GCC, with a release and a debug build type.

Inside the root directory, just run `conan test_package` or `conan test_package -s build_type=Debug`.

[1]: https://github.com/lasote/conan
[2]: https://bitbucket.org/scons/scons

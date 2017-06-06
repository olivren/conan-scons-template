# Conan SCons template

A template for a [Conan package manager][1] recipe, that uses [SCons][2] as its build tool instead of CMake.

This template demonstrates two different uses of SCons when writing a Conan recipe:
- Use SCons in the `test_package` part (the part that compiles a sample project to check that
  the library is correctly packaged and can be linked against)
- Use SCons to compile the library being packaged.

These two parts are independant one another. For example, it is perfectly fine to package a library
built with a Makefile, and use SCons for the `test_package` part.

This template supports Windows (MSVC) and Linux (GCC), and it supports a release and a debug build type.
The version of MSVC is hardcoded, and the coherence between the compiler setting of Conan (compiler, version
and arch), and the compiler detected by SCons is not checked.

Inside the root directory, just run `conan test_package` or `conan test_package -s build_type=Debug`.

[1]: https://github.com/lasote/conan
[2]: https://bitbucket.org/scons/scons

# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Adlbx(AutotoolsPackage):
    """ADLB/X: Master-worker library + work stealing and data dependencies"""

    homepage = 'http://swift-lang.org/Swift-T'
    url      = 'http://swift-lang.github.io/swift-t-downloads/spack/adlbx-0.0.0.tar.gz'
    git      = "https://github.com/swift-lang/swift-t.git"

    version('develop', branch='master')
    version('0.9.2', 'a7d9e208eb3b49b8bb857562f6bb61bb')
    version('0.9.1', '07151ddef5fb83d8f4b40700013d9daf')
    version('0.8.0', '34ade59ce3be5bc296955231d47a27dd')

    depends_on('exmcutils@develop', when='@develop')
    depends_on('exmcutils@:0.5.3', when='@:0.8.0')
    depends_on('exmcutils', when='@0.9.1:')
    depends_on('autoconf', type='build', when='@develop')
    depends_on('automake', type='build', when='@develop')
    depends_on('libtool', type='build', when='@develop')
    depends_on('m4', type='build', when='@develop')
    depends_on('mpi')

    def setup_environment(self, spack_env, run_env):
        spec = self.spec
        spack_env.set('CC', spec['mpi'].mpicc)
        spack_env.set('CXX', spec['mpi'].mpicxx)
        spack_env.set('CXXLD', spec['mpi'].mpicxx)

    @when('@develop')
    def configure_directory_helper(self):
        return "lb/code"

    @when('@0')
    def configure_directory_helper(self):
        return "."

    @property
    def configure_directory(self):
        return self.configure_directory_helper()

    def configure_args(self):
        args = ['--with-c-utils=' + self.spec['exmcutils'].prefix]
        return args

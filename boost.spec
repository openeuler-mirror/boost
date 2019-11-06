%global boost_docdir __tmp_docdir
%global boost_examplesdir __tmp_examplesdir
%global version_enc 1_66_0
%global toplev_dirname %{name}_%{version_enc}
%global sonamever %{version}

%bcond_with mpich
%bcond_with openmpi
%bcond_without context
%bcond_without python2
%bcond_without python3

%ifnarch %{ix86} x86_64
  %bcond_with quadmath
%else
  %bcond_without quadmath
%endif

%bcond_with tests
%bcond_with docs_generated

Name:           boost
Version:        1.66.0
Release:        16
Summary:        The free peer-reviewed portable C++ source libraries
License:        Boost and MIT and Python
URL:            http://www.boost.org
Source0:        https://sourceforge.net/projects/boost/files/boost/%{version}/%{toplev_dirname}.tar.bz2
Source1:        libboost_thread.so

# https://svn.boost.org/trac/boost/ticket/6150
Patch4:         boost-1.50.0-fix-non-utf8-files.patch

# http://www.boost.org/boost-build2/doc/html/bbv2/overview.html
Patch5:         boost-1.48.0-add-bjam-man-page.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=828856
# https://bugzilla.redhat.com/show_bug.cgi?id=828857
# https://svn.boost.org/trac/boost/ticket/6701
Patch15:        boost-1.58.0-pool.patch

# https://svn.boost.org/trac/boost/ticket/5637
Patch25:        boost-1.57.0-mpl-print.patch

# https://svn.boost.org/trac/boost/ticket/9038
Patch51:        boost-1.58.0-pool-test_linking.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1102667
Patch61:        boost-1.57.0-python-libpython_dep.patch
Patch62:        boost-1.66.0-python-abi_letters.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1190039
Patch65:        boost-1.66.0-build-optflags.patch

Patch68:        boost-1.66.0-address-model.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1318383
Patch82:        boost-1.66.0-no-rpath.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1541035
Patch83:        boost-1.66.0-bjam-build-flags.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1545092
Patch84:        boost-1.66.0-spirit-abs-overflow.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1585515
Patch85:        boost-1.66.0-compute.patch

# https://github.com/boostorg/python/pull/186
Patch86:        boost-1.66.0-python37.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1596468
# https://github.com/boostorg/python/pull/218
Patch87:        boost-1.66.0-numpy3.patch

Requires:       boost-atomic%{?_isa} = %{version}-%{release}
Requires:       boost-chrono%{?_isa} = %{version}-%{release}
Requires:       boost-container%{?_isa} = %{version}-%{release}
Requires:       boost-context%{?_isa} = %{version}-%{release}
Requires:       boost-coroutine%{?_isa} = %{version}-%{release}
Requires:       boost-date-time%{?_isa} = %{version}-%{release}
Requires:       boost-fiber%{?_isa} = %{version}-%{release}
Requires:       boost-filesystem%{?_isa} = %{version}-%{release}
Requires:       boost-graph%{?_isa} = %{version}-%{release}
Requires:       boost-iostreams%{?_isa} = %{version}-%{release}
Requires:       boost-locale%{?_isa} = %{version}-%{release}
Requires:       boost-log%{?_isa} = %{version}-%{release}
Requires:       boost-math%{?_isa} = %{version}-%{release}
Requires:       boost-program-options%{?_isa} = %{version}-%{release}
Requires:       boost-random%{?_isa} = %{version}-%{release}
Requires:       boost-regex%{?_isa} = %{version}-%{release}
Requires:       boost-serialization%{?_isa} = %{version}-%{release}
Requires:       boost-signals%{?_isa} = %{version}-%{release}
Requires:       boost-stacktrace%{?_isa} = %{version}-%{release}
Requires:       boost-system%{?_isa} = %{version}-%{release}
Requires:       boost-test%{?_isa} = %{version}-%{release}
Requires:       boost-thread%{?_isa} = %{version}-%{release}
Requires:       boost-timer%{?_isa} = %{version}-%{release}
Requires:       boost-type_erasure%{?_isa} = %{version}-%{release}
Requires:       boost-wave%{?_isa} = %{version}-%{release}

BuildRequires:  gcc-c++ m4 tcl
BuildRequires:  libstdc++-devel bzip2-devel zlib-devel
BuildRequires:  python2-devel python3-devel libicu-devel
BuildRequires:  python2-numpy python3-numpy
%if %{with quadmath}
BuildRequires:  libquadmath-devel
%endif

%description
Boost provides free peer-reviewed portable C++ source libraries. The
emphasis is on libraries which work well with the C++ Standard
Library. In order to establish "existing practice" and provide
reference implementations so that the Boost libraries are suitable
for eventual standardization. Ten Boost libraries are included in
the C++ Standards Committee's Library Technical Report (TR1) and in
the new C++11 Standard. C++11 also includes several more Boost
libraries in addition to those from TR1. More Boost libraries are
proposed for standardization in C++17.

%package atomic
Summary: C++11-style atomic<>

%description atomic

Boost.Atomic is a library that provides atomic data types and
operations on these data types, as well as memory ordering constraints
required for coordinating multiple threads through atomic variables.
It implements the interface as defined by the C++11 standard,but makes
this feature available for platforms lacking system/compiler support
for this particular C++11 feature.

%package chrono
Summary: Useful time utilities C++11
Requires: boost-system%{?_isa} = %{version}-%{release}

%description chrono

Boost.Chrono implements the new time facilities in C++11, as proposed in
N2661 - A Foundation to Sleep On. That document provides background and
motivation for key design decisions and is the source of a good deal of
information in this documentation. In addition to the clocks provided by
the standard proposal, Boost.Chrono provides specific process and thread
clocks.

%package container
Summary: Standard library containers and extensions

%description container

Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offer advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that don't comply with the latest
C++.

%package context
Summary: (C++11) Context switching library

%description context

Boost.Context is a foundational library that provides a sort of
cooperative multitasking on a single thread. By providing an abstraction
of the current execution state in the current thread, including the stack
(with local variables) and stack pointer, all registers and CPU flags,
and the instruction pointer, a execution context represents a specific
point in the application's execution path. This is useful for building
higher-level abstractions, like coroutines, cooperative threads
(userland threads) or an equivalent to C# keyword yield in C++.

%package coroutine
Summary: Run-time component of boost coroutine library

%description coroutine
Boost.Coroutine provides templates for generalized subroutines which
allow suspending and resuming execution at certain locations. It
preserves the local state of execution and allows re-entering
subroutines more than once (useful if state must be kept across function
calls).

%package date-time
Summary: A set of date-time libraries based on generic programming concepts

%description date-time

Boost Date Time is a set of date-time libraries based on generic
programming concepts.

%package fiber
Summary: (C++11) Userland threads library

%description fiber

Boost.Fiber provides a framework for micro-/userland-threads (fibers)
scheduled cooperatively. The API contains classes and functions to manage
and synchronize fibers similiarly to standard thread support library.

%package filesystem
Summary: Run-time component of boost filesystem library
Requires: boost-system%{?_isa} = %{version}-%{release}

%description filesystem

The Boost Filesystem Library provides portable facilities to query and
manipulate paths, files, and directories.

%package graph
Summary: Run-time component of boost graph library
Requires: boost-regex%{?_isa} = %{version}-%{release}

%description graph

BGL interface and graph components are generic, in the same sense as
the Standard Template Library (STL).

%package iostreams
Summary: Run-time component of boost iostreams library

%description iostreams

Boost.Iostreams provides a framework for defining streams, stream
buffers and i/o filters.

%package locale
Summary: Run-time component of boost locale library
Requires: boost-chrono%{?_isa} = %{version}-%{release}
Requires: boost-system%{?_isa} = %{version}-%{release}
Requires: boost-thread%{?_isa} = %{version}-%{release}

%description locale

Boost.Locale provide a set of localization and Unicode handling tools.

%package log
Summary: Run-time component of boost logging library

%description log

Boost.Log library aims to make logging significantly easier for the
application developer.  It provides a wide range of out-of-the-box
tools along with public interfaces for extending the library.

%package math
Summary: Math functions for boost TR1 library

%description math

Boost.Math includes several contributions in the domain of mathematics:
The Greatest Common Divisor and Least Common Multiple library provides
run-time and compile-time evaluation of the greatest common divisor
(GCD) or least common multiple (LCM) of two integers. The Special
Functions library currently provides eight templated special functions,
in namespace boost. The Complex Number Inverse Trigonometric Functions
are the inverses of trigonometric functions currently present in the C++
standard. Quaternions are a relative of complex numbers often used to
parameterise rotations in three dimentional space. Octonions, like
quaternions, are a relative of complex numbers.

%package numpy2
Summary: Run-time component of boost numpy library for Python 2
Requires: boost-python2%{?_isa} = %{version}-%{release}
Requires: python2-numpy
Provides: boost-numpy%{?_isa} = %{version}-%{release}
Obsoletes: boost-numpy < %{version}-%{release}

%description numpy2

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes,
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains run-time
support for the NumPy extension of the Boost Python Library for Python 2.

%package numpy3
Summary: Run-time component of boost numpy library for Python 3
Requires: boost-python3%{?_isa} = %{version}-%{release}
Requires: python3-numpy

%description numpy3

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes,
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains run-time
support for the NumPy extension of the Boost Python Library for Python 3.

%package program-options
Summary:  Run-time component of boost program_options library

%description program-options

Boost program options library allows program developers to obtain
(name, value) pairs from the user, via conventional methods such as
command line and config file.

%package python2
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Obsoletes: python2-%{name} < %{version}-%{release}
Summary: Run-time component of boost python library for Python 2

%description python2

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes,
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains run-time
support for the Boost Python Library compiled for Python 2.

%package python2-devel
Summary: Shared object symbolic links for Boost.Python 2
Requires: boost-numpy2%{?_isa} = %{version}-%{release}
Requires: boost-python2%{?_isa} = %{version}-%{release}
Requires: boost-devel%{?_isa} = %{version}-%{release}
Provides: boost-python-devel%{?_isa} = %{version}-%{release}
Obsoletes: boost-python-devel < %{version}-%{release}

%description python2-devel

Shared object symbolic links for Python 2 variant of Boost.Python.

%package python3
Summary: Run-time component of boost python library for Python 3

%description python3

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes,
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains run-time
support for the Boost Python Library compiled for Python 3.

%package python3-devel
Summary: Shared object symbolic links for Boost.Python 3
Requires: boost-numpy3%{?_isa} = %{version}-%{release}
Requires: boost-python3%{?_isa} = %{version}-%{release}
Requires: boost-devel%{?_isa} = %{version}-%{release}

%description python3-devel

Shared object symbolic links for Python 3 variant of Boost.Python.

%package random
Summary: A complete system for random number generation

%description random

The Boost Random Number Library provides a variety of generators and
distributions to produce random numbers having useful properties,
such as uniform distribution.

%package regex
Summary: Run-time component of boost regular expression library

%description regex

Regular expression library.

%package serialization
Summary: Run-time component of boost serialization library

%description serialization

Run-time support for serialization for persistence and marshaling.

%package signals
Summary: Run-time component of boost signals and slots library

%description signals

Managed signals & slots callback implementation (thread-safe version 2).

%package stacktrace
Summary: Run-time component of boost stacktrace library

%description stacktrace

Gather, store, copy and print backtraces.

%package system
Summary: Run-time component of boost system support library

%description system

Boost operating system support library, including the diagnostics support
that will be part of the C++0x standard library.

%package test
Summary: Run-time component of boost test library

%description test

Support for simple program testing, full unit testing, and for program
execution monitoring.

%package thread
Summary: Run-time component of boost thread library
Requires: boost-system%{?_isa} = %{version}-%{release}

%description thread

Boost.Thread enables the use of multiple threads of execution with shared
data in portable C++ code. It provides classes and functions for managing
the threads themselves, along with others for synchronizing data between
the threads or providing separate copies of data specific to individual
threads.

%package timer
Summary: Event timer, progress timer, and progress display classes
Requires: boost-chrono%{?_isa} = %{version}-%{release}
Requires: boost-system%{?_isa} = %{version}-%{release}

%description timer

"How long does my C++ code take to run?"
The Boost Timer library answers that question and does so portably,
with as little as one #include and one additional line of code.

%package type_erasure
Summary: Run-time component of boost type erasure library
Requires: boost-chrono%{?_isa} = %{version}-%{release}
Requires: boost-system%{?_isa} = %{version}-%{release}

%description type_erasure

The Boost.TypeErasure library provides runtime polymorphism in C++
that is more flexible than that provided by the core language.

%package wave
Summary: Run-time component of boost C99/C++ preprocessing library
Requires: boost-chrono%{?_isa} = %{version}-%{release}
Requires: boost-date-time%{?_isa} = %{version}-%{release}
Requires: boost-filesystem%{?_isa} = %{version}-%{release}
Requires: boost-system%{?_isa} = %{version}-%{release}
Requires: boost-thread%{?_isa} = %{version}-%{release}

%description wave

The Boost.Wave library is a Standards conforming, and highly
configurable implementation of the mandated C99/C++ preprocessor
functionality packed behind an easy to use iterator interface.

%package devel
Summary: The Boost C++ headers, shared and static development libraries and examples
Requires: boost%{?_isa} = %{version}-%{release}
Requires: libicu-devel%{?_isa}
%if %{with quadmath}
Requires: libquadmath-devel%{?_isa}
%endif
Provides: boost-static
Obsoletes: boost-static
Provides: boost-examples
Obsoletes: boost-examples

%description devel
Headers shared object symbolic links for the Boost C++ libraries and static
Boost C++ libraries, example source files distributed with boost.

%package help
Summary: HTML documentation for the Boost C++ libraries
BuildArch: noarch

%description help
This package contains the documentation in the HTML format of the Boost C++
libraries. The documentation provides the same content as that on the Boost
web page (http://www.boost.org/doc/libs/%{version_enc}).

%if 0%{with openmpi}
%package openmpi
Summary: Run-time component of Boost.MPI library
BuildRequires: openmpi-devel
Requires: boost-serialization%{?_isa} = %{version}-%{release}

%description openmpi

Run-time support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%package openmpi-devel
Summary: Shared library symbolic links for Boost.MPI
Requires: boost-devel%{?_isa} = %{version}-%{release}
Requires: boost-openmpi%{?_isa} = %{version}-%{release}
Requires: boost-graph-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel

Devel package for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%package openmpi-python2
Summary: Python 2 run-time component of Boost.MPI library
Requires: boost-openmpi%{?_isa} = %{version}-%{release}
Requires: boost-python%{?_isa} = %{version}-%{release}
Requires: boost-serialization%{?_isa} = %{version}-%{release}
Requires: python2-openmpi%{?_isa}
Provides: boost-openmpi-python%{?_isa} = %{version}-%{release}
Obsoletes: boost-openmpi-python < %{version}-%{release}

%description openmpi-python2

Python 2 support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%package openmpi-python2-devel
Summary: Shared library symbolic links for Boost.MPI Python 2 component
Requires: boost-devel%{?_isa} = %{version}-%{release}
Requires: boost-openmpi-devel%{?_isa} = %{version}-%{release}
Requires: boost-openmpi-python2%{?_isa} = %{version}-%{release}

%description openmpi-python2-devel

Devel package for the Python 2 interface of Boost.MPI-OpenMPI, a library
providing a clean C++ API over the OpenMPI implementation of MPI.

%package openmpi-python3
Summary: Python 3 run-time component of Boost.MPI library
Requires: boost-openmpi%{?_isa} = %{version}-%{release}
Requires: boost-python3%{?_isa} = %{version}-%{release}
Requires: boost-serialization%{?_isa} = %{version}-%{release}
Requires: python3-openmpi%{?_isa}

%description openmpi-python3

Python 3 support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%package openmpi-python3-devel
Summary: Shared library symbolic links for Boost.MPI Python 3 component
Requires: boost-devel%{?_isa} = %{version}-%{release}
Requires: boost-python3-devel%{?_isa} = %{version}-%{release}
Requires: boost-openmpi-devel%{?_isa} = %{version}-%{release}
Requires: boost-openmpi-python3%{?_isa} = %{version}-%{release}

%description openmpi-python3-devel

Devel package for the Python 3 interface of Boost.MPI-OpenMPI, a library
providing a clean C++ API over the OpenMPI implementation of MPI.

%package graph-openmpi
Summary: Run-time component of parallel boost graph library
Requires: boost-openmpi%{?_isa} = %{version}-%{release}
Requires: boost-serialization%{?_isa} = %{version}-%{release}

%description graph-openmpi

Run-time support for the Parallel BGL graph library.  The interface and
graph components are generic, in the same sense as the Standard
Template Library (STL).  This libraries in this package use OpenMPI
back-end to do the parallel work.
%endif

%if 0%{with mpich}
%package mpich
Summary: Run-time component of Boost.MPI library
BuildRequires: mpich-devel
Requires: boost-serialization%{?_isa} = %{version}-%{release}

%description mpich

Run-time support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%package mpich-devel
Summary: Shared library symbolic links for Boost.MPI
Requires: boost-devel%{?_isa} = %{version}-%{release}
Requires: boost-mpich%{?_isa} = %{version}-%{release}
Requires: boost-graph-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel

Devel package for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%package mpich-python2
Summary: Python run-time component of Boost.MPI library
Requires: boost-mpich%{?_isa} = %{version}-%{release}
Requires: boost-python2%{?_isa} = %{version}-%{release}
Requires: boost-serialization%{?_isa} = %{version}-%{release}
Requires: python2-mpich%{?_isa}
Provides: boost-mpich-python%{?_isa} = %{version}-%{release}
Obsoletes: boost-mpich-python < %{version}-%{release}

%description mpich-python2

Python 2 support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%package mpich-python2-devel
Summary: Shared library symbolic links for Boost.MPI Python 2 component
Requires: boost-devel%{?_isa} = %{version}-%{release}
Requires: boost-mpich-devel%{?_isa} = %{version}-%{release}
Requires: boost-mpich-python2%{?_isa} = %{version}-%{release}

%description mpich-python2-devel

Devel package for the Python 2 interface of Boost.MPI-MPICH, a library
providing a clean C++ API over the MPICH implementation of MPI.

%package mpich-python3
Summary: Python 3 run-time component of Boost.MPI library
Requires: boost-mpich%{?_isa} = %{version}-%{release}
Requires: boost-python3%{?_isa} = %{version}-%{release}
Requires: boost-serialization%{?_isa} = %{version}-%{release}
Requires: python3-mpich%{?_isa}

%description mpich-python3

Python 3 support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%package mpich-python3-devel
Summary: Shared library symbolic links for Boost.MPI Python 3 component
Requires: boost-devel%{?_isa} = %{version}-%{release}
Requires: boost-python3-devel%{?_isa} = %{version}-%{release}
Requires: boost-mpich-devel%{?_isa} = %{version}-%{release}
Requires: boost-mpich-python3%{?_isa} = %{version}-%{release}

%description mpich-python3-devel

Devel package for the Python 3 interface of Boost.MPI-MPICH, a library
providing a clean C++ API over the MPICH implementation of MPI.

%package graph-mpich
Summary: Run-time component of parallel boost graph library
Requires: boost-mpich%{?_isa} = %{version}-%{release}
Requires: boost-serialization%{?_isa} = %{version}-%{release}

%description graph-mpich

Run-time support for the Parallel BGL graph library.  The interface and
graph components are generic, in the same sense as the Standard
Template Library (STL).  This libraries in this package use MPICH
back-end to do the parallel work.

%endif

%package build
Summary: Cross platform build system for C++ projects
Requires: boost-jam
BuildArch: noarch

%description build
Boost.Build is an easy way to build C++ projects, everywhere. You name
your pieces of executable and libraries and list their sources.  Boost.Build
takes care about compiling your sources with the right options,
creating static and shared libraries, making pieces of executable, and other
chores -- whether you're using GCC, MSVC, or a dozen more supported
C++ compilers -- on Windows, OSX, Linux and commercial UNIX systems.

%package doctools
Summary: Tools for working with Boost documentation
Requires: docbook-dtds
Requires: docbook-style-xsl

%description doctools

Tools for working with Boost documentation in BoostBook or QuickBook format.

%package jam
Summary: A low-level build tool

%description jam
Boost.Jam (BJam) is the low-level build engine tool for Boost.Build.
Historically, Boost.Jam is based on on FTJam and on Perforce Jam but has grown
a number of significant features and is now developed independently.

%prep
%setup -q -n %{toplev_dirname}
find ./boost -name '*.hpp' -perm /111 | xargs chmod a-x

%patch4 -p1
%patch5 -p1
%patch15 -p0
%patch25 -p1
%patch51 -p1
%patch61 -p1
%patch62 -p1
%patch65 -p1
%patch68 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p2
%patch86 -p1
%patch87 -p1

%build
: PYTHON2_VERSION=%{python2_version}
PYTHON3_ABIFLAGS=$(/usr/bin/python3-config --abiflags)
: PYTHON3_VERSION=%{python3_version}
: PYTHON3_ABIFLAGS=${PYTHON3_ABIFLAGS}

export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-unused-local-typedefs -Wno-deprecated-declarations"
export RPM_LD_FLAGS

cat > ./tools/build/src/user-config.jam << "EOF"
import os ;
local RPM_OPT_FLAGS = [ os.environ RPM_OPT_FLAGS ] ;
local RPM_LD_FLAGS = [ os.environ RPM_LD_FLAGS ] ;

using gcc : : : <compileflags>$(RPM_OPT_FLAGS) <linkflags>$(RPM_LD_FLAGS) ;
%if 0%{with openmpi} || 0%{with mpich}
using mpi ;
%endif
using python : %{python2_version} : /usr/bin/python2 : /usr/include/python%{python2_version} : : : : ;
EOF

./bootstrap.sh --with-toolset=gcc --with-icu

echo ============================= build serial ==================
./b2 -d+2 -q %{?_smp_mflags} --without-mpi --without-graph_parallel \
  --build-dir=serial variant=release threading=multi debug-symbols=on \
  pch=off python=%{python2_version} stage

if [ $(find serial -type f -name has_atomic_flag_lockfree -print -quit | wc -l) -ne 0 ]; then
  DEF=D
else
  DEF=U
fi

m4 -${DEF}HAS_ATOMIC_FLAG_LOCKFREE -DVERSION=%{version} %{SOURCE1} > $(basename %{SOURCE1})

cat > python3-config.jam << "EOF"
import os ;
local RPM_OPT_FLAGS = [ os.environ RPM_OPT_FLAGS ] ;
local RPM_LD_FLAGS = [ os.environ RPM_LD_FLAGS ] ;

using gcc : : : <compileflags>$(RPM_OPT_FLAGS) <linkflags>$(RPM_LD_FLAGS) ;
%if 0%{with openmpi} || 0%{with mpich}
using mpi ;
%endif
EOF

cat >> python3-config.jam << EOF
using python : %{python3_version} : /usr/bin/python3 : /usr/include/python%{python3_version}${PYTHON3_ABIFLAGS} : : : : ${PYTHON3_ABIFLAGS} ;
EOF

echo ============================= build serial-py3 ==================
./b2 -d+2 -q %{?_smp_mflags} --user-config=./python3-config.jam \
  --with-python --build-dir=serial-py3 variant=release threading=multi \
  debug-symbols=on pch=off python=%{python3_version} stage

%if 0%{with openmpi} || 0%{with mpich}
module purge ||:
%endif

%if 0%{with openmpi}
%{_openmpi_load}
echo ============================= build $MPI_COMPILER ==================
./b2 -d+2 -q %{?_smp_mflags} --with-mpi --with-graph_parallel \
  --build-dir=$MPI_COMPILER variant=release threading=multi \
  debug-symbols=on pch=off python=%{python2_version} stage

echo ============================= build $MPI_COMPILER-py3 ==================
./b2 -d+2 -q %{?_smp_mflags} --user-config=./python3-config.jam \
  --with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER-py3 \
  variant=release threading=multi debug-symbols=on pch=off \
  python=%{python3_version} stage

%{_openmpi_unload}
export PATH=/bin${PATH:+:}$PATH
%endif

%if 0%{with mpich}
%{_mpich_load}
echo ============================= build $MPI_COMPILER ==================
./b2 -d+2 -q %{?_smp_mflags} --with-mpi --with-graph_parallel \
  --build-dir=$MPI_COMPILER variant=release threading=multi \
  debug-symbols=on pch=off python=%{python2_version} stage

echo ============================= build $MPI_COMPILER-py3 ==================
./b2 -d+2 -q %{?_smp_mflags} --user-config=./python3-config.jam \
  --with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER-py3 \
  variant=release threading=multi debug-symbols=on pch=off \
  python=%{python3_version} stage

%{_mpich_unload}
export PATH=/bin${PATH:+:}$PATH
%endif

echo ============================= build Boost.Build ==================
(cd tools/build
 ./bootstrap.sh --with-toolset=gcc)

%check
:

%install
cd %{_builddir}/%{toplev_dirname}

%if 0%{with openmpi} || 0%{with mpich}
module purge ||:
%endif


%if 0%{with openmpi}
%{_openmpi_load}
echo ============================= install $MPI_COMPILER ==================
./b2 -q %{?_smp_mflags} --with-mpi --with-graph_parallel \
  --build-dir=$MPI_COMPILER --stagedir=${RPM_BUILD_ROOT}${MPI_HOME} \
  variant=release threading=multi debug-symbols=on pch=off \
  python=%{python2_version} stage

mkdir -p ${RPM_BUILD_ROOT}%{python2_sitearch}/openmpi/boost
touch ${RPM_BUILD_ROOT}%{python2_sitearch}/openmpi/boost/__init__.py
mv ${RPM_BUILD_ROOT}${MPI_HOME}/lib/mpi.so \
   ${RPM_BUILD_ROOT}%{python2_sitearch}/openmpi/boost/

echo ============================= install $MPI_COMPILER-py3 ==================
./b2 -q %{?_smp_mflags} --user-config=./python3-config.jam \
  --with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER-py3 \
  --stagedir=${RPM_BUILD_ROOT}${MPI_HOME} variant=release \
  threading=multi debug-symbols=on pch=off \
  python=%{python3_version} stage

mkdir -p ${RPM_BUILD_ROOT}%{python3_sitearch}/openmpi/boost
touch ${RPM_BUILD_ROOT}%{python3_sitearch}/openmpi/boost/__init__.py
mv ${RPM_BUILD_ROOT}${MPI_HOME}/lib/mpi.so ${RPM_BUILD_ROOT}%{python3_sitearch}/openmpi/boost/

rm -f ${RPM_BUILD_ROOT}${MPI_HOME}/lib/libboost_{python,{w,}serialization}*

%{_openmpi_unload}
export PATH=/bin${PATH:+:}$PATH
%endif

%if 0%{with mpich}
%{_mpich_load}
echo ============================= install $MPI_COMPILER ==================
./b2 -q %{?_smp_mflags} --with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER \
  --stagedir=${RPM_BUILD_ROOT}${MPI_HOME} variant=release threading=multi\
  debug-symbols=on pch=off python=%{python2_version} stage

mkdir -p ${RPM_BUILD_ROOT}%{python2_sitearch}/mpich/boost
touch ${RPM_BUILD_ROOT}%{python2_sitearch}/mpich/boost/__init__.py
mv ${RPM_BUILD_ROOT}${MPI_HOME}/lib/mpi.so ${RPM_BUILD_ROOT}%{python2_sitearch}/mpich/boost/

echo ============================= install $MPI_COMPILER-py3 ==================
./b2 -q %{?_smp_mflags} --user-config=./python3-config.jam \
  --with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER-py3 \
  --stagedir=${RPM_BUILD_ROOT}${MPI_HOME} variant=release threading=multi \
  debug-symbols=on pch=off python=%{python3_version} stage

mkdir -p ${RPM_BUILD_ROOT}%{python3_sitearch}/mpich/boost
touch ${RPM_BUILD_ROOT}%{python3_sitearch}/mpich/boost/__init__.py
mv ${RPM_BUILD_ROOT}${MPI_HOME}/lib/mpi.so ${RPM_BUILD_ROOT}%{python3_sitearch}/mpich/boost/

rm -f ${RPM_BUILD_ROOT}${MPI_HOME}/lib/libboost_{python,{w,}serialization}*

%{_mpich_unload}
export PATH=/bin${PATH:+:}$PATH
%endif

echo ============================= install serial ==================
./b2 -d+2 -q %{?_smp_mflags} --without-mpi --without-graph_parallel \
  --build-dir=serial --prefix=$RPM_BUILD_ROOT%{_prefix} \
  --libdir=$RPM_BUILD_ROOT%{_libdir} \
  variant=release threading=multi debug-symbols=on pch=off \
  python=%{python2_version} install

[ -f $RPM_BUILD_ROOT%{_libdir}/libboost_thread.so ]
rm -f $RPM_BUILD_ROOT%{_libdir}/libboost_thread.so
install -p -m 644 $(basename %{SOURCE1}) $RPM_BUILD_ROOT%{_libdir}/

echo ============================= install serial-py3 ==================
./b2 -d+2 -q %{?_smp_mflags} --user-config=python3-config.jam \
  --with-python --build-dir=serial-py3 --prefix=$RPM_BUILD_ROOT%{_prefix} \
  --libdir=$RPM_BUILD_ROOT%{_libdir} variant=release threading=multi \
  debug-symbols=on pch=off python=%{python3_version} install

echo ============================= install Boost.Build ==================
(cd tools/build
 ./b2 --prefix=$RPM_BUILD_ROOT%{_prefix} install
 chmod -x $RPM_BUILD_ROOT%{_datadir}/boost-build/src/build/alias.py
 chmod +x $RPM_BUILD_ROOT%{_datadir}/boost-build/src/tools/doxproc.py
 rm -f $RPM_BUILD_ROOT%{_bindir}/b2
 rm -f $RPM_BUILD_ROOT%{_datadir}/boost-build/src/build/project.ann.py
 rm -f $RPM_BUILD_ROOT%{_datadir}/boost-build/src/tools/doxygen/windows-paths-check.hpp
 %{__install} -p -m 644 v2/doc/bjam.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/bjam.1
)

echo ============================= install Boost.QuickBook ==================
(cd tools/quickbook
 ../build/b2 --prefix=$RPM_BUILD_ROOT%{_prefix}
 %{__install} -p -m 755 ../../dist/bin/quickbook $RPM_BUILD_ROOT%{_bindir}/
 cd ../boostbook
 find dtd -type f -name '*.dtd' | while read tobeinstalledfiles; do
   install -p -m 644 $tobeinstalledfiles -D $RPM_BUILD_ROOT%{_datadir}/boostbook/$tobeinstalledfiles
 done
 find xsl -type f | while read tobeinstalledfiles; do
   install -p -m 644 $tobeinstalledfiles -D $RPM_BUILD_ROOT%{_datadir}/boostbook/$tobeinstalledfiles
 done
)

echo ============================= install documentation ==================
rm -rf %{boost_docdir} && %{__mkdir_p} %{boost_docdir}/html
DOCPATH=%{boost_docdir}
DOCREGEX='.*\.\(html?\|css\|png\|gif\)'

find libs doc more -type f -regex $DOCREGEX | sed -n '/\//{s,/[^/]*$,,;p}' | sort -u > tmp-doc-directories

sed "s:^:$DOCPATH/:" tmp-doc-directories | xargs -P 0 --no-run-if-empty %{__install} -d

cat tmp-doc-directories | while read tobeinstalleddocdir; do
  find $tobeinstalleddocdir -mindepth 1 -maxdepth 1 -regex $DOCREGEX -print0 \
  | xargs -P 0 -0 %{__install} -p -m 644 -t $DOCPATH/$tobeinstalleddocdir
done
rm -f tmp-doc-directories
%{__install} -p -m 644 -t $DOCPATH LICENSE_1_0.txt index.htm index.html boost.png rst.css boost.css

echo ============================= install examples ==================
sed -i -e 's/\r//g' libs/geometry/example/ml02_distance_strategy.cpp
for tmp_doc_file in flyweight/example/Jamfile.v2 \
  format/example/sample_new_features.cpp multi_index/example/Jamfile.v2 \
  multi_index/example/hashed.cpp serialization/example/demo_output.txt
do
  mv libs/${tmp_doc_file} libs/${tmp_doc_file}.iso8859
  iconv -f ISO8859-1 -t UTF8 < libs/${tmp_doc_file}.iso8859 > libs/${tmp_doc_file}
  touch -r libs/${tmp_doc_file}.iso8859 libs/${tmp_doc_file}
  rm -f libs/${tmp_doc_file}.iso8859
done

rm -rf %{boost_examplesdir} && mkdir -p %{boost_examplesdir}/html
EXAMPLESPATH=%{boost_examplesdir}
find libs -type d -name example -exec find {} -type f \; | sed -n '/\//{s,/[^/]*$,,;p}' | sort -u > tmp-doc-directories
sed "s:^:$EXAMPLESPATH/:" tmp-doc-directories | xargs -P 0 --no-run-if-empty %{__install} -d
rm -f tmp-doc-files-to-be-installed && touch tmp-doc-files-to-be-installed
cat tmp-doc-directories | while read tobeinstalleddocdir
do
  find $tobeinstalleddocdir -mindepth 1 -maxdepth 1 -type f >> tmp-doc-files-to-be-installed
done
cat tmp-doc-files-to-be-installed | while read tobeinstalledfiles
do
  if test -s $tobeinstalledfiles; then
    tobeinstalleddocdir=`dirname $tobeinstalledfiles`
    %{__install} -p -m 644 -t $EXAMPLESPATH/$tobeinstalleddocdir $tobeinstalledfiles
  fi
done
rm -f tmp-doc-files-to-be-installed
rm -f tmp-doc-directories
%{__install} -p -m 644 -t $EXAMPLESPATH LICENSE_1_0.txt

%post doctools
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
  "http://www.boost.org/tools/boostbook/dtd" \
  "file://%{_datadir}/boostbook/dtd" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
  "http://www.boost.org/tools/boostbook/dtd" \
  "file://%{_datadir}/boostbook/dtd" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
  "http://www.boost.org/tools/boostbook/xsl" \
  "file://%{_datadir}/boostbook/xsl" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
  "http://www.boost.org/tools/boostbook/xsl" \
  "file://%{_datadir}/boostbook/xsl" $CATALOG

%postun doctools
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del "file://%{_datadir}/boostbook/dtd" $CATALOG
  %{_bindir}/xmlcatalog --noout --del "file://%{_datadir}/boostbook/xsl" $CATALOG
fi


%files
%license LICENSE_1_0.txt

%files atomic
%license LICENSE_1_0.txt
%{_libdir}/libboost_atomic.so.%{sonamever}

%files chrono
%license LICENSE_1_0.txt
%{_libdir}/libboost_chrono.so.%{sonamever}

%files container
%license LICENSE_1_0.txt
%{_libdir}/libboost_container.so.%{sonamever}

%files context
%license LICENSE_1_0.txt
%{_libdir}/libboost_context.so.%{sonamever}

%files coroutine
%license LICENSE_1_0.txt
%{_libdir}/libboost_coroutine.so.%{sonamever}

%files date-time
%license LICENSE_1_0.txt
%{_libdir}/libboost_date_time.so.%{sonamever}

%files fiber
%license LICENSE_1_0.txt
%{_libdir}/libboost_fiber.so.%{sonamever}

%files filesystem
%license LICENSE_1_0.txt
%{_libdir}/libboost_filesystem.so.%{sonamever}

%files graph
%license LICENSE_1_0.txt
%{_libdir}/libboost_graph.so.%{sonamever}

%files iostreams
%license LICENSE_1_0.txt
%{_libdir}/libboost_iostreams.so.%{sonamever}

%files locale
%license LICENSE_1_0.txt
%{_libdir}/libboost_locale.so.%{sonamever}

%files log
%license LICENSE_1_0.txt
%{_libdir}/libboost_log.so.%{sonamever}
%{_libdir}/libboost_log_setup.so.%{sonamever}

%files math
%license LICENSE_1_0.txt
%{_libdir}/libboost_math_c99.so.%{sonamever}
%{_libdir}/libboost_math_c99f.so.%{sonamever}
%{_libdir}/libboost_math_c99l.so.%{sonamever}
%{_libdir}/libboost_math_tr1.so.%{sonamever}
%{_libdir}/libboost_math_tr1f.so.%{sonamever}
%{_libdir}/libboost_math_tr1l.so.%{sonamever}

%files numpy2
%license LICENSE_1_0.txt
%{_libdir}/libboost_numpy.so.%{sonamever}

%files numpy3
%license LICENSE_1_0.txt
%{_libdir}/libboost_numpy3.so.%{sonamever}

%files test
%license LICENSE_1_0.txt
%{_libdir}/libboost_prg_exec_monitor.so.%{sonamever}
%{_libdir}/libboost_unit_test_framework.so.%{sonamever}

%files program-options
%license LICENSE_1_0.txt
%{_libdir}/libboost_program_options.so.%{sonamever}

%files python2
%license LICENSE_1_0.txt
%{_libdir}/libboost_python.so.%{sonamever}

%files python2-devel
%license LICENSE_1_0.txt
%{_libdir}/libboost_numpy.so
%{_libdir}/libboost_python.so

%files python3
%license LICENSE_1_0.txt
%{_libdir}/libboost_python3.so.%{sonamever}

%files python3-devel
%license LICENSE_1_0.txt
%{_libdir}/libboost_numpy3.so
%{_libdir}/libboost_python3.so

%files random
%license LICENSE_1_0.txt
%{_libdir}/libboost_random.so.%{sonamever}

%files regex
%license LICENSE_1_0.txt
%{_libdir}/libboost_regex.so.%{sonamever}

%files serialization
%license LICENSE_1_0.txt
%{_libdir}/libboost_serialization.so.%{sonamever}
%{_libdir}/libboost_wserialization.so.%{sonamever}

%files signals
%license LICENSE_1_0.txt
%{_libdir}/libboost_signals.so.%{sonamever}

%files stacktrace
%license LICENSE_1_0.txt
%{_libdir}/libboost_stacktrace_addr2line.so.%{sonamever}
%{_libdir}/libboost_stacktrace_basic.so.%{sonamever}
%{_libdir}/libboost_stacktrace_noop.so.%{sonamever}

%files system
%license LICENSE_1_0.txt
%{_libdir}/libboost_system.so.%{sonamever}

%files thread
%license LICENSE_1_0.txt
%{_libdir}/libboost_thread.so.%{sonamever}

%files timer
%license LICENSE_1_0.txt
%{_libdir}/libboost_timer.so.%{sonamever}

%files type_erasure
%license LICENSE_1_0.txt
%{_libdir}/libboost_type_erasure.so.%{sonamever}

%files wave
%license LICENSE_1_0.txt
%{_libdir}/libboost_wave.so.%{sonamever}

%files help
%doc %{boost_docdir}/*

%files devel
%exclude %{_libdir}/libboost_numpy3.so
%exclude %{_libdir}/libboost_numpy.so
%exclude %{_libdir}/libboost_python3.so
%exclude %{_libdir}/libboost_python.so
%license LICENSE_1_0.txt
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.a
%if 0%{with mpich}
%{_libdir}/mpich/lib/*.a
%endif
%if 0%{with openmpi}
%{_libdir}/openmpi/lib/*.a
%endif
%doc %{boost_examplesdir}/*

%if 0%{with openmpi}
%files openmpi
%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi.so.%{sonamever}

%files openmpi-devel
%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi.so
%{_libdir}/openmpi/lib/libboost_graph_parallel.so


%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi_python.so.%{sonamever}
%{python2_sitearch}/openmpi/boost/

%files openmpi-python2-devel
%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi_python.so

%files openmpi-python3
%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi_python3.so.%{sonamever}
%{python3_sitearch}/openmpi/boost/

%files openmpi-python3-devel
%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi_python3.so


%files graph-openmpi
%license LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_graph_parallel.so.%{sonamever}
%endif

%if 0%{with mpich}
%files mpich
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi.so.%{sonamever}

%files mpich-devel
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi.so
%{_libdir}/mpich/lib/libboost_graph_parallel.so

%files mpich-python2
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi_python.so.%{sonamever}
%{python2_sitearch}/mpich/boost/

%files mpich-python2-devel
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi_python.so

%files mpich-python3
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi_python3.so.%{sonamever}
%{python3_sitearch}/mpich/boost/

%files mpich-python3-devel
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi_python3.so

%files graph-mpich
%license LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_graph_parallel.so.%{sonamever}

%endif

%files build
%license LICENSE_1_0.txt
%{_datadir}/boost-build/

%files doctools
%license LICENSE_1_0.txt
%{_bindir}/quickbook
%{_datadir}/boostbook/

%files jam
%license LICENSE_1_0.txt
%{_bindir}/bjam
%{_mandir}/man1/bjam.1*

%changelog
* Mon Oct 28 2019 caomeng <caomeng5@huawei.com> - 1.66.0-16
- Type:NA
- ID:NA
- SUG:NA
- DESC:add bcondwith openmpi and mpich

* Wed Aug 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.66.0-15
- Package init

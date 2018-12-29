%define base_name llvm
%global ver_major_minor 6.0
Name: %{base_name}%{ver_major_minor}
Version: %{ver_major_minor}.0
%define src_dir %{base_name}-60
Release: 0%{?dist}
Summary: The Low Level Virtual Machine
License: NCSA
Group: Development/Languages
URL: http://llvm.org
BuildRequires: git cmake
BuildRequires: gcc
BuildRequires: gcc-c++ libstdc++-static
BuildRequires: clang
BuildRequires: llvm%{ver_major_minor}-devel llvm%{ver_major_minor}-static 
BuildRequires: glibc-devel     
BuildRequires: glibc
BuildRequires: zlib-devel
%undefine _disable_source_fetch
Source0: https://hephaistos.lpp.polytechnique.fr/data/mirrors/llvm/%{src_dir}.tar.gz
%define  SHA256SUM0 b9ab616f41dc3ae85ac013cc7511d309f0c6f739a1c926afbd096f61c6773ebd
%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary programming
languages. The compiler infrastructure includes mirror sets of programming
tools as well as libraries with equivalent functionality.
	
%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%setup -qn %{src_dir}

%build
mkdir build && cd build
CC=clang CXX=clang++ cmake -DBUILD_SHARED_LIBS:BOOL=false -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo -DCMAKE_INSTALL_PREFIX:PATH=%{_usr}/local/%{base_name}-%{ver_major_minor} ..

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} -C build


%files
%{_usr}/local/%{base_name}-%{ver_major_minor}/*

%changelog

* Fri Dec 28 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 6.0.0-0
- First setup


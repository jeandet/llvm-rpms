%define base_name llvm
%global ver_major_minor 7.0
Name: %{base_name}%{ver_major_minor}
Version: %{ver_major_minor}.0
%define src_dir %{base_name}-70
Release: 0%{?dist}
Summary: The Low Level Virtual Machine
License: NCSA
Group: Development/Languages
URL: http://llvm.org
BuildRequires: git cmake
BuildRequires: gcc
BuildRequires: gcc-c++ libstdc++-static
BuildRequires: clang
BuildRequires: glibc-devel     
BuildRequires: glibc
BuildRequires: zlib-devel
%undefine _disable_source_fetch
Source0: https://hephaistos.lpp.polytechnique.fr/data/mirrors/llvm/%{src_dir}.tar.gz
%define  SHA256SUM0 5568883f825c5f8e58e5ff0c71a5fa23528f4de30c892294d9f7833aa38da273
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

* Sun Dec 30 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 7.0.0-0
- First setup


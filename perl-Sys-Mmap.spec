#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sys-Mmap
Version  : 0.20
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Sys-Mmap-0.20.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/Sys-Mmap-0.20.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsys-mmap-perl/libsys-mmap-perl_0.19-1.debian.tar.xz
Summary  : 'uses mmap to map in a file as a Perl variable'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Sys-Mmap-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Mmap perl module, version alpha2
This program is free software; you can redistribute it and/or modify
it under the terms of either:

%package dev
Summary: dev components for the perl-Sys-Mmap package.
Group: Development
Provides: perl-Sys-Mmap-devel = %{version}-%{release}
Requires: perl-Sys-Mmap = %{version}-%{release}

%description dev
dev components for the perl-Sys-Mmap package.


%package perl
Summary: perl components for the perl-Sys-Mmap package.
Group: Default
Requires: perl-Sys-Mmap = %{version}-%{release}

%description perl
perl components for the perl-Sys-Mmap package.


%prep
%setup -q -n Sys-Mmap-0.20
cd %{_builddir}
tar xf %{_sourcedir}/libsys-mmap-perl_0.19-1.debian.tar.xz
cd %{_builddir}/Sys-Mmap-0.20
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sys-Mmap-0.20/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sys::Mmap.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Sys/Mmap.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Sys/Mmap/Mmap.so

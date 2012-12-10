%define major 2
%define tarball_name towitoko
%define libname %mklibname %{tarball_name} %major

Summary: CT-API and PCSC-Lite driver for Towitoko smart card readers
Name: %{libname}
Version: 2.0.7
Release: 8
License: GPL
Group: System/Libraries
Source0: http://www.geocities.com/cprados/files/%{tarball_name}-%{version}.tar.gz
Source1: towitoko.conf
URL: http://www.geocities.com/cprados/
Requires(post): pcsc-lite

%description
This library provides a driver for using Towitoko smartcard readers under UNIX
environment.

%package devel
Summary: Development files for Towitoko smart card readers
Group: Development/C
Requires: %{name} = %{version}
Provides: libtowitoko-devel = %{EVRD}

%description devel
This package contains header files and development libraries for
Towitoko smartcard readers.

%prep
%setup -q -n %{tarball_name}-%{version}

%build
aclocal
autoconf
%configure
%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}/reader.conf.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/reader.conf.d/

%post
%{_sbindir}/update-reader.conf
if [ "$1" -eq "1" ]; then
	echo
	echo "Please configure %{_sysconfdir}/reader.conf.d/towitoko.conf"
	echo
fi

%postun
%{_sbindir}/update-reader.conf

%files
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/reader.conf.d/towitoko.conf
%{_libdir}/lib*.so.*
%{_bindir}/*

%files devel
%doc ChangeLog doc/*.html
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*




%changelog
* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.0.7-7mdv2011.0
+ Revision: 436485
- rebuild
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Sep 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-09-29 20:35:32 (62768)
- added default config file (#23142)

* Fri Sep 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-09-29 20:19:02 (62767)
- Import libtowitoko2

* Wed May 17 2006 Andras Hasenack <andreas@mandriva.com> 2.0.7-2mdk
- fix x86_64 build: libtool was being generated incorrectly

* Thu Nov 24 2005 Andreas Hasenack <andreas@mandriva.com> 2.0.7-1mdk
- packaged for Mandriva


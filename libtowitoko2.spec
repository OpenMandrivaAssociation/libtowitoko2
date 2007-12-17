%define major 2
%define tarball_name towitoko
%define libname %mklibname %{tarball_name} %major

Summary: CT-API and PCSC-Lite driver for Towitoko smart card readers
Name: %{libname}
Version: 2.0.7
Release: %mkrel 3
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
Provides: libtowitoko-devel = %{version}-%{release}

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}/reader.conf.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/reader.conf.d/

%post
/sbin/ldconfig
%{_sbindir}/update-reader.conf
if [ "$1" -eq "1" ]; then
	echo
	echo "Please configure %{_sysconfdir}/reader.conf.d/towitoko.conf"
	echo
fi

%postun
/sbin/ldconfig
%{_sbindir}/update-reader.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/reader.conf.d/towitoko.conf
%{_libdir}/lib*.so.*
%{_bindir}/*

%files devel
%defattr(-,root,root)
%doc ChangeLog doc/*.html
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man3/*



Summary:	DevHelp book: glibc
Summary(pl):	Ksi±¿ka do DevHelpa o glibc
Name:		devhelp-book-glibc
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/glibc.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about glibc.

%description -l pl
Ksi±¿ka do DevHelpa o glibc.

%prep
%setup -q -c -n glibc

rm -rf book/CVS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/books/libc-2.2.3

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/books/libc-2.2.3/libc-2.2.3.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/libc-2.2.3

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*

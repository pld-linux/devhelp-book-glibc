Summary:	DevHelp book: glibc
Summary(pl):	Ksi±¿ka do DevHelp'a o glibc
Name:		devhelp-book-glibc
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/glibc.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp/

%description
DevHelp book about glibc

%description -l pl
Ksi±¿ka do DevHelp o glibc

%prep
%setup -q -c glibc -n glibc

%build
mv -f book glibc
mv -f book.devhelp glibc.devhelp
rm -rf glibc/CVS

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}/books/libc-2.2.3
install -d $RPM_BUILD_ROOT%{_prefix}/specs
install glibc.devhelp $RPM_BUILD_ROOT%{_prefix}/specs
install glibc/* $RPM_BUILD_ROOT%{_prefix}/books/libc-2.2.3

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/books
%{_prefix}/specs

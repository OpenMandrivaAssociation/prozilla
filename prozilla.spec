%define name	prozilla
%define version	2.0.4
%define release	%mkrel 6

Summary:	A multithreaded download accelerator
Name:		%name
Version:	%version
Release:	%release
License: 	GPL
URL:		http://prozilla.genesys.ro/
Group:		Networking/File transfer
Source:		http://prozilla.genesys.ro/downloads/prozilla/tarballs/%{name}-%{version}.tar.bz2
Patch0:		prozilla_download_win.h.patch.bz2
BuildRoot:	%_tmppath/%{name}-buildroot
Buildrequires:	ncurses-devel

%description
ProZilla is a multithreaded download accelerator for Linux which supports
both HTTP and FTP protocols. It makes multiple connections to the server 
and downloads the file in portions, thus giving a much better speed rate 
than the conventional download programs which use a single connection. 
Resuming connections is fully supported and customisable.

%package devel
Summary:	Header files and development files for %{name}
Group:		Networking/File transfer
Requires:	%{name}

%description devel
Header files and development files for %{name}

%prep
rm -rf %buildroot
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
aclocal
autoconf
automake

%configure
%make

%install
%makeinstall

# (mpol) remove unwanted locale files
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/.mo
if [ -f %{buildroot}%{_datadir}/locale/locale.alias ]
	then
	rm -f %{buildroot}%{_datadir}/locale/locale.alias
fi

%find_lang proz


%clean
rm -rf %buildroot

%files -f proz.lang
%defattr (-,root,root)
%doc AUTHORS ChangeLog CREDITS COPYING NEWS README TODO
%_bindir/*
%_mandir/man1/*

%files devel
%defattr (-,root,root)
%{_includedir}/*
%{_libdir}/*.*a

Summary:	A multithreaded download accelerator
Name:		prozilla
Version:	2.0.4
Release:	9
License: 	GPLv2+
Group:		Networking/File transfer
Url:		http://prozilla.genesys.ro/
Source0:	http://prozilla.genesys.ro/downloads/prozilla/tarballs/%{name}-%{version}.tar.bz2
Patch0:		prozilla_download_win.h.patch
BuildRequires:	pkgconfig(ncurses)

%description
ProZilla is a multithreaded download accelerator for Linux which supports
both HTTP and FTP protocols. It makes multiple connections to the server
and downloads the file in portions, thus giving a much better speed rate
than the conventional download programs which use a single connection.
Resuming connections is fully supported and customisable.

%files
%doc AUTHORS ChangeLog CREDITS COPYING NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%package devel
Summary:	Header files and development files for %{name}
Group:		Networking/File transfer

%description devel
Header files and development files for %{name}

%files devel
%{_includedir}/*
%{_libdir}/*.a

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

# (mpol) remove unwanted locale files
rm -f %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/.mo
[ -f %{buildroot}%{_datadir}/locale/locale.alias ] && rm -f %{buildroot}%{_datadir}/locale/locale.alias



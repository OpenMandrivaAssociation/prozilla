%define name	prozilla
%define version	2.0.4
%define release	%mkrel 7

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


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0.4-7mdv2010.0
+ Revision: 441962
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 2.0.4-6mdv2009.1
+ Revision: 350203
- 2009.1 rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.4-5mdv2009.0
+ Revision: 259324
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.4-4mdv2009.0
+ Revision: 247231
- rebuild

* Mon Feb 18 2008 Antoine Ginies <aginies@mandriva.com> 2.0.4-2mdv2008.1
+ Revision: 172305
- bump release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 22 2007 Antoine Ginies <aginies@mandriva.com> 2.0.4-1mdv2008.0
+ Revision: 29695
- build fix
- Import prozilla




* Wed Apr 26 2006 Lenny Cartier <lenny@mandriva.com> 2.0.4-1mdk
- 2.0.4

* Wed Jan 18 2006 Marcel Pol <mpol@mandriva.org> 2.0.2-2mdk
- remove %%{_datadir}/locale/locale.alias if it exists

* Fri Dec 02 2005 Marcel Pol <mpol@mandriva.org> 2.0.2-1mdk
- 2.0.2
- add devel package
- update filelist
- remove unwanted locale files

* Fri Mar 25 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.3.7-2mdk
- .4 subrelease

* Mon Jan 24 2005 Erwna Velu <velu@seanodes.com> 1.3.7-1mdk
- 1.3.7.3

* Fri May 14 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.3.6-6mdk
- rebuild

* Thu Apr  3 2003 Stew Benedict <sbenedict@mandrakesoft.com> 1.3.6-5mdk
- new URL, Source link

* Mon Dec 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 1.3.6-4mdk
- rebuild for new glibc/rpm, installed but unpackaged files

* Wed Mar 06 2002 Yves Duret <yduret@mandrakesoft.com> 1.3.6-3mdk
- spec clean up, macro, rpmlint
- added buildrequires on ncurses-devel

* Fri Aug 31 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.3.6-2mdk
- s/Copyright/License/

* Fri Aug 24 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.6-1mdk
- 1.3.6.

* Mon Aug  6 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5.2-2mdk
- Remove empty %%post/%%postun.

* Mon Aug  6 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5.2-1mdk
- 1.3.5.2.
- Really Fix URL.

* Mon Jun 25 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5.1-1mdk
- Fix URL.
- 1.3.5.1.
- Fix files.

* Thu Jan 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.06pre1-1mdk
- updated to 1.06pre1

* Wed Jan 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.06pre0-1mdk
- new in contribs

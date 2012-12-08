%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 2.2_20050523-0

%define languageenglazy Italian
%define languagecode it
%define lc_ctype it_IT

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.54.0
Release:       %mkrel 10
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/it/aspell6-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:	   spell-it

Autoreqprov:   no

Obsoletes: ispell-it, ispell-italian

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n aspell6-%{languagecode}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv README README.%{languagecode}
chmod 644 README* Copyright doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.54.0-9mdv2011.0
+ Revision: 662842
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.54.0-8mdv2011.0
+ Revision: 603409
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.54.0-7mdv2010.1
+ Revision: 518935
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.54.0-6mdv2010.0
+ Revision: 413078
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.54.0-5mdv2009.1
+ Revision: 350041
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.54.0-4mdv2009.0
+ Revision: 220390
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.54.0-3mdv2008.1
+ Revision: 182478
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.54.0-2mdv2008.1
+ Revision: 148803
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.54.0-1mdv2007.0
+ Revision: 123281
- Import aspell-it

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.54.0-1mdv2007.1
- use the mkrel macro
- disable debug packages

* Wed Nov 02 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.54.0-1mdk
- new release

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.53.0-2mdk
- rebuild for new aspell

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.53.0-1mdk
- 0.53

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.52.0-1mdk
- updated dictionnary


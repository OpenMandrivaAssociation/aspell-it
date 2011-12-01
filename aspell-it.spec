%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 2.2_20050523-0

%define languageenglazy Italian
%define languagecode it
%define lc_ctype it_IT

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.54.0
Release:       %mkrel 9
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
rm -fr %{buildroot}

%makeinstall_std

mv README README.%{languagecode}
chmod 644 README* Copyright doc/*

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*



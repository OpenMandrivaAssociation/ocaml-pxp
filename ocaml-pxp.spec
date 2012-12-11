%define up_name pxp
%define name	ocaml-%{up_name}
%define version	1.2.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A validating parser for XML
Source0:	http://download.camlcity.org/download/%{up_name}-%{version}.tar.gz
URL:		http://www.ocaml-programming.de/packages/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-pcre-devel
BuildRequires:  ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PXP  is a validating parser for XML-1.0 which has been written entirely in
Objective Caml.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:   %{name} = %{version}-%{release}

%description	devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
./configure
make all opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
make install OCAMLFIND_DESTDIR="%{buildroot}/%{_libdir}/ocaml"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE doc/*
%{_libdir}/ocaml/*
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmi
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.cmxa

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa


%changelog
* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.1-1mdv2010.0
+ Revision: 385116
- BuildRequires
- updated version

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.test2.3mdv2009.1
+ Revision: 321072
- don't forget devel -> main package dependency

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.test2.2mdv2009.1
+ Revision: 321013
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Fri Mar 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-0.test2.1mdv2008.1
+ Revision: 181225
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 07 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.0-0.test1.1mdv2008.0
+ Revision: 36936
- new release: 1.2.0test1


* Thu Feb 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.96-1mdv2007.0
+ Revision: 124722
- new version

* Wed Feb 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.6-1mdv2007.1
+ Revision: 124093
- fix build dependencies

* Wed Feb 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.6-1mdv2007.1
- first mdv release


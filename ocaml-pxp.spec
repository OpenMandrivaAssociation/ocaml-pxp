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

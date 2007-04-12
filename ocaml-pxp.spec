%define up_name pxp
%define name	ocaml-%{up_name}
%define version	1.1.96
%define release	%mkrel 1
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A validating parser for XML
Source: 	http://www.ocaml-programming.de/packages/%{up_name}-%{version}.tar.bz2
Patch:      %{name}-1.1.96-destdir.patch
URL:		http://www.ocaml-programming.de/packages/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PXP  is a validating parser for XML-1.0 which has been written entirely in
Objective Caml.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch -p 1

%build
./configure
make all opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE doc/*
%{ocaml_sitelib}/*



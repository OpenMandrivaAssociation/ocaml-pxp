%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	An XML parser for OCaml
Name:		ocaml-pxp
Version:	1.2.4
Release:	2
License:	MIT
Group:		Development/Other
Url:		http://projects.camlcity.org/projects/pxp.html
Source0:	http://download.camlcity.org/download/pxp-%{version}.tar.gz
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-ulex-devel
Requires:	ocaml-ulex

%description
PXP is an XML parser for OCaml. It represents the parsed document either as
tree or as stream of events. In tree mode, it is possible to validate the
XML document against a DTD.

The acronym PXP means Polymorphic XML Parser. This name reflects the ability
to create XML trees with polymorphic type parameters.

%files
%doc LICENSE README
%dir %{_libdir}/ocaml/pxp/
%{_libdir}/ocaml/pxp/META
%dir %{_libdir}/ocaml/pxp-engine/
%{_libdir}/ocaml/pxp-engine/META
%{_libdir}/ocaml/pxp-engine/*.cmi
%{_libdir}/ocaml/pxp-engine/*.cma
%{_libdir}/ocaml/pxp-engine/*.cmo
%dir %{_libdir}/ocaml/pxp-pp/
%{_libdir}/ocaml/pxp-pp/META
%{_libdir}/ocaml/pxp-pp/pxp_pp.cma
%dir %{_libdir}/ocaml/pxp-lex-iso88591/
%dir %{_libdir}/ocaml/pxp-lex-iso885910/
%dir %{_libdir}/ocaml/pxp-lex-iso885913/
%dir %{_libdir}/ocaml/pxp-lex-iso885914/
%dir %{_libdir}/ocaml/pxp-lex-iso885915/
%dir %{_libdir}/ocaml/pxp-lex-iso885916/
%dir %{_libdir}/ocaml/pxp-lex-iso88592/
%dir %{_libdir}/ocaml/pxp-lex-iso88593/
%dir %{_libdir}/ocaml/pxp-lex-iso88594/
%dir %{_libdir}/ocaml/pxp-lex-iso88595/
%dir %{_libdir}/ocaml/pxp-lex-iso88596/
%dir %{_libdir}/ocaml/pxp-lex-iso88597/
%dir %{_libdir}/ocaml/pxp-lex-iso88598/
%dir %{_libdir}/ocaml/pxp-lex-iso88599/
%dir %{_libdir}/ocaml/pxp-lex-utf8/
%{_libdir}/ocaml/pxp-lex-*/META
%{_libdir}/ocaml/pxp-lex-*/*.cmi
%{_libdir}/ocaml/pxp-lex-*/*.cmo
%{_libdir}/ocaml/pxp-lex-*/*.cma
%{_libdir}/ocaml/pxp-lex-*/*.o
%dir %{_libdir}/ocaml/pxp-ulex-utf8/
%{_libdir}/ocaml/pxp-ulex-utf8/META
%{_libdir}/ocaml/pxp-ulex-utf8/*.cmi
%{_libdir}/ocaml/pxp-ulex-utf8/*.cmo
%{_libdir}/ocaml/pxp-ulex-utf8/*.cma
%{_libdir}/ocaml/pxp-ulex-utf8/*.o

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	ocaml-ulex-devel

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc doc/
%doc examples/
%doc rtests/
%doc tools/
%{_libdir}/ocaml/pxp-*/*.a
%{_libdir}/ocaml/pxp-*/*.cmxa
%{_libdir}/ocaml/pxp-*/*.cmx
%{_libdir}/ocaml/pxp-*/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n pxp-%{version}

%build
./configure

make all opt
make doc

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/pxp
make install


Name:		texlive-begingreek
Version:	63255
Release:	2
Summary:	Greek environment to be used with pdfLaTeX only
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/begingreek
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begingreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begingreek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/begingreek.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This simple package defines a greek environment to be used with
pdfLaTeX only, that accepts an optional Greek font family name
to type its contents with. A similar \greektxt command does a
similar action for shorter texts.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/begingreek
%{_texmfdistdir}/tex/latex/begingreek
%doc %{_texmfdistdir}/doc/latex/begingreek

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

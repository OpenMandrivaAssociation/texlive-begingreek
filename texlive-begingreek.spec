%global tl_name begingreek
%global tl_revision 63255

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Greek environment to be used with pdfLaTeX only
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/begingreek
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/begingreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/begingreek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/begingreek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This simple package defines a greek environment to be used with pdfLaTeX
only, that accepts an optional Greek font family name to type its
contents with. A similar \greektxt command does a similar action for
shorter texts.


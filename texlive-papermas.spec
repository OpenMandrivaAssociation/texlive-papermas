%global tl_name papermas
%global tl_revision 78632

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Compute the mass of a printed version of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/papermas
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package computes the number of sheets of paper used by, and hence
the mass of a document. This is useful (for example) when calculating
postal charges.


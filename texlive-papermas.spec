Name:		texlive-papermas
Version:	23667
Release:	1
Summary:	Compute the mass of a printed version of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/papermas
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package computes the number of sheets of paper used by, and
the mass of a document. This is useful (for example) when
calculating postal charges.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/papermas/papermas.sty
%doc %{_texmfdistdir}/doc/latex/papermas/README
%doc %{_texmfdistdir}/doc/latex/papermas/papermas-example.pdf
%doc %{_texmfdistdir}/doc/latex/papermas/papermas-example.tex
%doc %{_texmfdistdir}/doc/latex/papermas/papermas.pdf
#- source
%doc %{_texmfdistdir}/source/latex/papermas/papermas.drv
%doc %{_texmfdistdir}/source/latex/papermas/papermas.dtx
%doc %{_texmfdistdir}/source/latex/papermas/papermas.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

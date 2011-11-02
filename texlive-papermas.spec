Name:		texlive-papermas
Version:	1.0h
Release:	1
Summary:	Compute the mass of a printed version of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/papermas
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/papermas.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package computes the number of sheets of paper used by, and
the mass of a document. This is useful (for example) when
calculating postal charges.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

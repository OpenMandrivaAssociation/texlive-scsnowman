Name:		texlive-scsnowman
Version:	66115
Release:	1
Summary:	Snowman variants using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scsnowman
License:	bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scsnowman.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scsnowman.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides a command \scsnowman which can
display many variants of "snowman" ("yukidaruma" in Japanese).
TikZ is required for drawing these snowmen.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/scsnowman
%doc %{_texmfdistdir}/doc/latex/scsnowman

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

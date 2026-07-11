%global tl_name scsnowman
%global tl_revision 66115

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3c
Release:	%{tl_revision}.1
Summary:	Snowman variants using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/scsnowman
License:	bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scsnowman.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scsnowman.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides a command \scsnowman which can display many
variants of "snowman" ("yukidaruma" in Japanese). TikZ is required for
drawing these snowmen.


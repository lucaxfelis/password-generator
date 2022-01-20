# password-generator :lock_with_ink_pen:

Script Python que gera uma senha de várias complexidades e copia para o clipboard

## Instalação

### Usuário Linux  :warning:

Se você utiliza alguma distro Linux, você precisa instalar o pacote xclip:

```
emerge xclip # Gentoo, Funtoo, ...
sudo apt install xclip # Debian, Ubuntu, Mint, ...
sudo pacman -S xclip # Arch, Manjaro, ...
sudo dnf install xclip # Red Hat, CentOS, Fedora, ...
```

Você também pode instalá-lo clonando o repositório oficial no GitHub:

```
git clone https://github.com/astrand/xclip
cd xclip
./configure
sudo make install
```
### Todos os usuários

Então, você deve clonar este repositório:

```
git clone https://github.com/lucaxfelis/password-generator.git
```

Em seguida, no diretório do script, você deve instalar os pacotes requeridos:

```
pip install -r /(path-to-password-generator)/requirements.txt
```

Depois vocẽ deve executar o arquivo "main.py":

```
python /(path-to-password-generator)/main.py
```
**Obs: substituir o "path-to-password-generator" pelo caminho correto.**

### Clipboard

No fim da execução, sua senha estará no clipboard, pronta para ser colada em qualquer campo.

{ pkgs, lib, config, inputs, ... }:

{
  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    package = pkgs.python313Full;
    venv.enable = true;
  };

  enterShell = ''
  '';
  
  
  # https://devenv.sh/services/
  # services.postgres.enable = true;


  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}

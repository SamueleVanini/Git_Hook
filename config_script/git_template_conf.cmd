@ECHO OFF
set @path_from=%~dp0
set @path_from=%@path_from:\config_script=\hooks%
set @path_from=%@path_from%*.*
set @path_to=%~dp0
set @path_to=%@path_to:\Git_Hook\config_script=\.git\hooks%
copy %@path_from% %@path_to%
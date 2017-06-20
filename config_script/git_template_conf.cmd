@ECHO OFF
set @path_from=%~dp0
set @path_from=%@path_from:\config_script=\hooks%
set @path_from=%@path_from%pre-commit
set @path_to=%~dp0
set @path_to=%@path_to:\Git_Hook-master\config_script=\.git\hooks%
set @file_orig=%@path_to%pre-commit
for /R %@path_to% %%A in (*) do (
    if  "%%~nxA" EQU "pre-commit" (
        copy %@file_orig%+%@path_from% %@path_to%
        exit(0)
    )
)
copy %@path_from% %@path_to%

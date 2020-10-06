import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import time 
df = pd.read_csv('diabetic_data.csv')
abc = """ 
                                                                                                                                  



















----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*.........................&@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@% ...........................&@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@*.... @@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@#.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@% ...........................@@@@@@@@@@@@& ......................@@@@@@@& ...........................&@@@@@@@@
@@@@@@@@@@@@@*.........................@@@@@@@@@@@@@@@#....................@@@@@@@@@@(.........................&@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@ .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@ .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@ .      ,@@@@.      .@@@@,      @@/.       @@@/       (@@@. @@@@@@@*       #@@@..     .*@@@@       *@@@@@@@@@@
@@@@@@@@@@ .@@@@@@.#@@@@@@@@@& (@@%.%@@@@@@& (@@@@@@@@@@./@@@@@/ @@@. @@@@@@@.#@@@@@. @@@..@@@@@(.&@@@@@@@@@%.&@@@@@@@@@
@@@@@@@@@@ .@@@@@@.#@@/ &&&&&% (@@%.%@@@@@@& (@@@@@@@@@@ *&&&&&&@@@@. @@@@@@@.#@@@@@. @@@. @@@@@(.&@@ ,&&&&&#.&@@@@@@@@@
@@@@@@@@@@..#####(.#@@/ #####( #@@%.%@@@@@@@.*#######@@@ *#######@@@. ####%@@ /#####..@@@. @@@@@(.&@@..#####( &@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@













                                                                                                                                  
                       (&@&&&&&&&&&&&@@.      *&&&&&&&&&&&&&&&&.   /&&&&&&&&&&&&&&&&&&&&&&.        ,//(////.                      
                     &@&&&&&@@@@@@@&&@%      &&&&&&@&&&&&&@@@&%    /&&&&&&&&&&&&&&&&&&&&&&.      .(((//((///(.                    
                    #&&&&&/                 (&&&&&                          &&&&&(               //((((((((((,                    
                    @&&&&%                  (&&&&&                          &&&&&(               .(((//((/((/                     
                    @&&&&%                  *&&&&&%*                        &&&&&(                 .///(/(/                       
                    @&&&&%                   /&&&&&&&&&&&&%/.               &&&&&(                                                
                    @&&&&%                       ,#&&&&&&&&&@&&.            &&&&&(                                                
                    @&&&&%                               ,&&&&&%            &&&&&(                  */((//,                       
                    @&&&&%                                (&&&&&            &&&&&(               ./(/(((((/(/                     
                    #&&&&@(                               %@&&&%            &&&&&(               /((((((((((/,                    
                     %&&&&&&&&@@@@&&&&%     (&&&&&&&&%&&&&&&&&&,            &&&&&(               ,(((/((///((.                    
                       /&@&&&&&&&&&&&&@.    %&&&&&&&&&&&&&&@&/              &&&&&(                 /(((/(/(*                      
                                                                                                                                  
                                                                                                                                  
                    ,/*                         */.                               ,(/.                                            
                    &  *,/,(/(.,(,( #.#(/,,  /   ,(./( #/#.( ,* %*,*##./  **/.%/.  /. %/ #(# %#*.(( ,#*.(/ (#                     
                                                                                                                                  
                                                                                                                                  









@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@











----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------



























"""                                                                                                                                                                                                                         
print (abc)
poli = """
Esto es una version beta para demostración - testML.py utilizando una Base de Datos del Departamento se Salud 
del gobierno de EE.UU.  de dominio publico (usa.health.gov) con datos de ingreso de  130 hospitales federales 
 para poner a prueba nuestro modelo de Machine Learning en el contexto de una enfermedad cronica como la DM1/2 
 con el objetivo de reducir la tasa de reingresos hospitaarios que posteriormente integraremos en una base de 
 Datos de nuestro medio con otras enfermedades cronicas prevalentes como EPOC, IC ... 
 
 
 
 Octubre / 2020
 
 Terrassa, Barcelona
 """

print (poli)



xyz = """

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@/.     .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@,     ...   . (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,      /@@@@@
@@@@%    ########(   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#        .#(    &@@@
@@@@.   ##########(   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.   .      (##*   (@@@
@@@@,   ##########(   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/    *@@@@@/        %@@@@
@@@@&    /#######,   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&     &@@@@@@@@@@@@@@@@@@@@@
@@@@@@%                 .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/    *@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@#*,,,/%@@@@&,    .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.    %@@@@@@@@@@@@@@@@&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@,     (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%/,*#@@@@@@@@@@@@@(    *@@@@@@@@@@@@@@@( .      %@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@#     ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         #@@@@@@@@.    &@@@@@@@@@.          (##*   #@@@
@@@@@@@@*     .   (@@@@@@@@@@@@&.    .&@*        .#@@@@@@@@@@@@@   .///,   &@@@@/    *@@@@@@@@@/    .,,,,.   ,((.   %@@@
@@@@@%    .,/(/,    .@@@@@@@@@@@@@@,      .*(#/.    .@@@@@@@@@@@   .///,   ,**.    %@@@@@@@@&.  . %@@@@@@@@.      ,@@@@@
@@@@/   *#########.   &@@@@@@@@@@@@@*   (#########.   @@@@@@@@@@   .///,        ,@@@@@@@@@/    ,@@@@@@@@@@@@@@@@@@@@@@@@
@@@@    ###########.          .        ,###########                .///,   &@@@@@@@@@@@@     %@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@*   ##########*   (&&&&&&&&&&&&&,   ##########,   #&&&&&&&&&   .///,   &@@@@@@@@@(    *@@@@@@@@@@@@@@@@@&/**(&@@@@@@
@@@@@,.   (#####*     (@@@@@@@@@@@@@,  .  ######*    #@@@@@@@@@@   .///,.             . @@@@@@@@@@@@@@@@@@.       .*@@@@
@@@@@@@/           /     ,@@@@@@&.    .*      .    %@@@@@@@@@@@@   .///,   ........../@@@@@@@@@@@*           ####   (@@@
@@@@@@@@@@@@&&&@@@@@@@&.    .(     *@@@@@@@@&&&@@@@@@@@@#   &@@@   .///,   &@@@@@@@@@@@@@@@@@@&    .%&&&&%    ,.    @@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@.     /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .///,   &@@@@@@@@@@@@@@@@*    /@@@@@@@@@%      @@@@@@
@@@@@@@@@@@@@@@@@@@@@@@.    ./     /@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .///,         .            .&@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@/          .(.    ,@@@@@@#   . ,/          .%@@@@#   &@@@   .///,   %&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@*    /#####,     *@@@@@@@@@@@@&.     (#####,    %@@@@@@@@@@   .///,   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.    *@@@@@@
@@@@*   ##########*   (@@@@@@@@@@@@@,   ##########,   %@@@@@@@@@   .///,   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&          @@@@
@@@@ .  ###########.    .              ,########### .              .///,        .             .             .####   (@@@
@@@@/   *#########.   %@@@@@@@@@@@@@*   (#########.   @@@@@@@@@@   .///, . &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.        *@@@@
@@@@@#     *(#(,       %@@@@@@@@@@@*      ./##(,    .@@@@@@@@@@@  ..///,   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&*  /@@@@@@@
@@@@@@@@*         (@(     /@@@@&,    .%&,         (@@@@@#   &@@@   .///,   ,*****************&@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@#          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .///,                       /@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@/       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .///,   &@@@@@@@@@@@@@@@@&   . &@@@@@@@@.      /@@@@@
@@@@@@@@@@%*,,*/&@@@@@,     #@*     (@@@@@#*,,*/&@@@@@@@#   &@@@   .///,   &@@@@@@@@@@@@@@@@@@@/    ,,,,,,   ,(/    %@@@
@@@@@@%                 .&@@@@@@@(                 ,@@@@@@@@@@@@   .///,.             %@@@@@@@@@@&.          (##/   #@@@
@@@@@   .*#######.   ,@@@@@@@@@@@@@@%    (#######  . *@@@@@@@@@@ . .///,  .             .@@@@@@@@@@@@@@@@@*     .  %@@@@
@@@@, . ##########(   .,,,,,,,,,,,,,.  .##########/   .,,,,,,,,,   .///,.  &@@@@@@@@@&.    %@@@@@@@@@@@@@@@@@@&&@@@@@@@@
@@@@.   ###########.                   ,###########                .///,   &@@@@@@@@@@@@(    *@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@#    #########   .@@@@@@@@@@@@@@(   .########(   .@@@@@@@@@@   .///,         &@@@@@@@@@.    &@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@. .  ....     /@@@@@@@@@@@@@/      . ....     (@@@@@@@@@@@   .///,   %&&(    *@@@@@@@@@(    ,@@@@@@@/    .   %@@@@
@@@@@@@@@*.     ./@@@@@@@@@@@@@*    .#@@&*.     ,(@@@@@@@@@@@@@@&         #@@@@@@.    %@@@@@@@@@.            (##*   #@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&.     &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.../@@@@@@@@@@@/    ,@@@@@@@@@(......    ,#(    %@@@
@@@@@@@@@@@@@@@@@@@@@@@@#     ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.    %@@@@@@@@@@@@@@@.      *@@@@@
@@@@@@@@@/.     ,#@@@/     (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(    *@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@,     ...         %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.    &@@@@@@@@@@@@@@@@@@@@@@@
@@@@%    ########(   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  . ,@@@@@@@@@&/..(@@@@@@@
@@@@.   ##########(   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     %@@@@.     .  *@@@@
@@@@.   ##########(   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/          ####   (@@@
@@@@&    /#######.   ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&          @@@@
@@@@@@#         .  .&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.    ,&@@@@@
@@@@@@@@@@#,,,,*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@





"""


df.info()
print(df.head())

print(df.groupby('discharge_disposition_id').size())
df = df.loc[~df.discharge_disposition_id.isin([11,13,14,19,20,21])]
df['OUTPUT_LABEL'] = (df.readmitted == '<30').astype('int')
def calc_prevalence(y_actual):
    return (sum(y_actual)/len(y_actual))
print('Prevalence:%.3f'%calc_prevalence(df['OUTPUT_LABEL'].values))
print('Number of columns:',len(df.columns))
print (df[list(df.columns)[:10]].head())
print (df[list(df.columns)[10:20]].head())
print (df[list(df.columns)[20:30]].head())
print (df[list(df.columns)[30:40]].head())
print (df[list(df.columns)[40:]].head())
# para cada columna
for c in list(df.columns):
    
    # crear lista de valores unicos
    n = df[c].unique()
    
    # si el numero de valores es inferior a 30, mostrar los mismos en pantallas, en caso contrario mostrar el numero de valores unicos
    if len(n)<30:
        print(c)
        print(n)
    else:
        print(c + ': ' +str(len(n)) + ' unique values')
# replace ? with nan
df = df.replace('?',np.nan)
# columns that are numerical that we will use
cols_num = ['time_in_hospital','num_lab_procedures', 'num_procedures', 'num_medications',
       'number_outpatient', 'number_emergency', 'number_inpatient','number_diagnoses']
df[cols_num].isnull().sum()
print(df[cols_num].isnull().sum())
# conversion de non-numerical a variables con la tecnica one-hot encoding,-- categorical data we will deal with are these columns
cols_cat = ['race', 'gender', 
       'max_glu_serum', 'A1Cresult',
       'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide',
       'glimepiride', 'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide',
       'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone',
       'tolazamide', 'insulin',
       'glyburide-metformin', 'glipizide-metformin',
       'glimepiride-pioglitazone', 'metformin-rosiglitazone',
       'metformin-pioglitazone', 'change', 'diabetesMed','payer_code']
df[cols_cat].isnull().sum()
print (df[cols_cat].isnull().sum())
# race, payer_code, and medical_specialty have missing data. Since these are categorical data, usaremosla funcion fill N/A .
df['race'] = df['race'].fillna('UNK')
df['payer_code'] = df['payer_code'].fillna('UNK')
df['medical_specialty'] = df['medical_specialty'].fillna('UNK')
print('Number medical specialty:', df.medical_specialty.nunique())
df.groupby('medical_specialty').size().sort_values(ascending = False)
print (df.groupby('medical_specialty').size().sort_values(ascending = False))
# We can see that most of them are unknown and that the count drops off pretty quickly. 
# We don't want to add 73 new variables since some of them only have a few samples.
#  As an alternative, we can create a new variable that only has 11 options 
# (the top 10 specialities and then an other category). 
# Obviously, there are other options for bucketing, but this is one of the easiest methods.

#BUCKETING  (RECLASIFICAR LAS ESPECIALIDADES)

top_10 = ['UNK','InternalMedicine','Emergency/Trauma',\
          'Family/GeneralPractice', 'Cardiology','Surgery-General' ,\
          'Nephrology','Orthopedics',\
          'Orthopedics-Reconstructive','Radiologist']

# make a new column with duplicated data
df['med_spec'] = df['medical_specialty'].copy()

# replace all specialties not in top 10 with 'Other' category
df.loc[~df.med_spec.isin(top_10),'med_spec'] = 'Other'
df.groupby('med_spec').size()
cols_cat_num = ['admission_type_id', 'discharge_disposition_id', 'admission_source_id']

df[cols_cat_num] = df[cols_cat_num].astype('str')
df_cat = pd.get_dummies(df[cols_cat + cols_cat_num + ['med_spec']],drop_first = True)
df_cat.head()
print (df_cat.head())
df = pd.concat([df,df_cat], axis = 1)
cols_all_cat = list(df_cat.columns)
df[['age', 'weight']].head()
print (df[['age', 'weight']].head())
df.groupby('age').size()
print (df.groupby('age').size())
age_id = {'[0-10)':0, 
          '[10-20)':10, 
          '[20-30)':20, 
          '[30-40)':30, 
          '[40-50)':40, 
          '[50-60)':50,
          '[60-70)':60, 
          '[70-80)':70, 
          '[80-90)':80, 
          '[90-100)':90}
df['age_group'] = df.age.replace(age_id)
df.weight.notnull().sum()
print(df.weight.notnull().sum())
df['has_weight'] = df.weight.notnull().astype('int')
cols_extra = ['age_group','has_weight']

qwe = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@,  .. .(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   /@@
@@. #####( ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@. .   #* (@
@@&  ####  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&  &@@@@@@@@@@
@@@@@#,,%@@,  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  @@@@@@@@&@@@@
@@@@@@@@@@@@@@#  ,@@@@@@@@@@@@@@@    #@@@@  &@@@@.     #* #@
@@@  .//  .@@@@@@@   .(/  .@@@@@  //  *.  @@@@& .%@@@@   ,@@
@@  ######     .    ######        //  @@@@@@   @@@@@@@@@@@@@
@@@. (##*  (@@@@@@,  ###*  @@@@@  //.      .@@@@@@@@@.   .@@
@@@@@@&&@@@&  .   @@@@&&@@@@# &@  //  @@@@@@@@@&  %&&  ,  @@
@@@@@@@@@@@@  .   @@@@@@@@@@@@@@  //           .@@@@@@@@@@@@               Resumen de Ingeniería de features ''características ''
@@@  /##,  *@@@@@@.  (##,  @@@@@  //  @@@@@@@@@@@@@@@@.  @@@
@@  ######  .       ######.       //    .      .      .## (@
@@@   ((    @@@@@@   .#(  .@@@@@ .//  @@@@@@@@@@@@@@@@& /@@@
@@@@@@@@@@@@     .@@@@@@@@@@@@@@  //            @@@@@@@@@@@@
@@@@@%,*&@@,  #*  (@@#,*&@@@# &@  //  @@@@@@@@@@  ,,,  (  %@
@@@ .####  @@@@@@@%  ####  @@@@@  // .      .@@@@@@@@*  . @@
@@. ######          ######        //  @@@@@@(  @@@@@@@@@@@@@                Previo a la construccion del modelo
@@@.. ..  /@@@@@@/    ..  (@@@@@  //  &(  @@@@@  ,@@@/    @@
@@@@@@@@@@@@@@.  &@@@@@@@@@@@@@@@@..@@@@@@  ,@@@@(...  #  %@
@@@@@.  ,@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(  @@@@@@@@@@@@@       Estabilización , pre-normalizacion y chequeo de falta/ perdida de valores / datos
@@%  ####  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .,@@@@&.(@@@
@@. #####( *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/     ## (@
@@@#    . &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  &@@
"""

print (qwe)


print('Total number of features:', len(cols_num + cols_all_cat + cols_extra))
print('Numerical Features:',len(cols_num))
print('Categorical Features:',len(cols_all_cat))
print('Extra features:',len(cols_extra))


col2use = cols_num + cols_all_cat + cols_extra
df_data = df[col2use + ['OUTPUT_LABEL']]


asd = """ - Training samples: these samples are used to train the model
- Validation samples: these samples are held out from the training data and are used to make decisions on how to improve the model
- Test samples: these samples are held out from all decisions and are used to measure the generalized performance of the model
"""

print (asd)
print  (qwe)
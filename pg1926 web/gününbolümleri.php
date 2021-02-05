<?php


$t=date("H");

if($t=="06"or $t=="07"or $t=="08"or $t=="09"or $t=="10")
{
    echo '<script type="text/javascript">';
    echo 'alert("Günaydın")';  
    echo '</script>';

}
else if($t=="11"or $t=="12"or $t=="13"or $t=="14"or $t=="15"or $t=="16"or $t=="17")
{
    echo '<script type="text/javascript">';
    echo 'alert("İyi günler")';  
    echo '</script>';

}
else if($t=="18"or $t=="19"or $t=="20")
{
    echo '<script type="text/javascript">';
    echo 'alert("İyi akşamlar")';  
    echo '</script>';


}
else if($t=="21"or $t=="22"or $t=="23"or $t=="00")
{
    echo '<script type="text/javascript">';
    echo 'alert("İyi geceler")';  
    echo '</script>';

}
else
{ 
    
    echo '<script type="text/javascript">';
    echo 'alert("Esenlikler dilerim")';  
    echo '</script>';


}
echo date("H");

?>
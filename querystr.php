<html>
<head>
    <style>
.textstyle {
			font-size:2.5vw;
            color: purple; 
			font-family: "Lucida Console";
			text-shadow: 5px 5px 5px pink;
            height: 10%;
		}

img {
    border-radius: 50%;
}
    </style>
</head>
<?php

$file_name = fopen("query.txt", 'w');
$qury=$_GET["message"];
fwrite($file_name, $qury);
fclose($file_name);


?>
<body style="display: flex;  align-items: center ; justify-content: center; background-color:#ccf5ff;">

    <div class="textstyle"> 
        Your query is being searched ...  <br />
    </div>
    <div style="height = 90%;">
        <img src="bun1.gif" alt="searcnhing your query" height="400px" width="400px"  align="center">
    </div>
</body>
</html>

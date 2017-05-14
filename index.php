<?php
/*
 * index.php
 * 
 * Copyright 2017 raja <raja@raja-Inspiron-N5110>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

?>
<html>
	<head>
        <style>
		.button{
			background-color: #4CAF50;
			border: none;
			color: white;
			padding: 15px 32px;
			text-align: center;
			text-decoration: none;
			display: inline-block;
			font-size: 16px;
			margin 4px 2px;
			cursor: pointer;
			border: 3px solid white;
		}
		#alerts{
			margin: auto;
			width: 50%;
			text-align: center;
			font-size: 24px;
		}
		#btn_list{
			margin: auto;
			width: 25%;
		}
		#cam_container{
			margin: auto;
			width: 50%;
		}
	</style>
	<script src="jquery-3.1.1.js"></script>
	<script type ="text/javascript">
                $(document).ready(function(){
			$('#MailMe').click(function(){
				$('#response').text("Mailing your picture. Please wait...");
				$.ajax({
					type: 'Post',
					url: 'Mail_script.php',
					success: function(data3){
						$('#response').text(data3);
					}
				});
			});
			$('#cam_container').hide();
                        $('#Print').click(function(){
                                $.ajax({
                                        type: 'Post',
                                        url : 'Print_script.php',
                                        success: function(data){
                                                $('#response').text(data);
						$('#cam_container').hide();
                                        }
                                });
                        });
			$('#start_preview').click(function(){
				$('#response').text("Starting camera. Please wait..");
				$.ajax({
					type: 'Post',
					url: 'Click_script.php',
					success: function(data2){
						$('#cam_container').show();
						$('#cam_stream').attr('src', window.location.protocol + '//' + window.location.hostname + ':8090/stream');
						$('#response').text(data2);
					}
				/**$("#response").text("Smile! Clicking Picture");
				$('#cam_stream').attr('src', window.location.protocol + '//' + window.location.hostname + ':8090/stream');
				**/
				});
			});
		});
        </script>
	</head>
	<body>
		<div id="btn_list">
			<button id="PhotoLere" class="button" type="button">Click my Photo. Photo lere!</button>
			<button id="Print" class="button" type="button">Print my Picture</button>
			<button id="Mailme" class="button" type="button">Mail My Pic</button>
		</div>
		<div id="alerts">
			<p id="response"></p>
		</div>
		<div id="cam_container">
			<img id="cam_stream" src="stream" width "640" height="480" />
		</div>
	</body>
</html>

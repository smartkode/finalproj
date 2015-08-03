#!/usr/bin/php
 
<?php
# CHANGE DIRECTORIES TO MATCH A SUITABLE ONE FOR YOUR ENVIRONMENT
$log = '/home/rascal/Documents/FinalProject/daemon/log/Daemon.log';
 
/**
 * Method for displaying the help and default variables.
 **/
function displayUsage(){
    global $log;
 
    echo "n";
    echo "Process for demonstrating a PHP daemon.n";
    echo "n";
    echo "Usage:n";
    echo "tDaemon.php [options]n";
    echo "n";
    echo "toptions:n";
    echo "tt--help display this help messagen";
    echo "tt--log=<filename> The location of the log file (default '$log')n";
    echo "n";
}//end displayUsage()
 
//configure command line arguments
if($argc > 0){
    foreach($argv as $arg){
        $args = explode('=',$arg);
        switch($args[0]){
            case '--help':
                return displayUsage();
            case '--log':
                $log = $args[1];
                break;
        }//end switch
    }//end foreach
}//end if
 
//fork the process to work in a daemonized environment
file_put_contents($log, "Status: starting up.n", FILE_APPEND);
$pid = pcntl_fork();
if($pid == -1){
	file_put_contents($log, "Error: could not daemonize process.n", FILE_APPEND);
	return 1; //error
}
else if($pid){
	return 0; //success
}
else{
    //the main process
    $run = 1;
    while($run<2){
        file_put_contents($log, 'Running...', FILE_APPEND);
        $user = "root";
		$database = "search_1";
		$hostname = "localhost";
		$password = "RenVenrascal";
		mysql_connect($hostname, $user, $password) or die ("Database connection failed.");
		mysql_select_db($database) or die ("Database selection failed.");
		echo "string";
		
		//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		// taken from "Search.php"

		// $start_search = getmicrotime();
	   //initializing MySQL Query  
	   $sql_query = mysql_query("SELECT * FROM news WHERE MATCH(title,article) AGAINST('politics')");

	   //additional check. Insurance method to re-search the database again in case of too many matches (too many matches cause returning of 0 results)
	   	if($results = mysql_num_rows($sql_query) != 0) {
	   		mysql_query("SELECT * FROM news WHERE MATCH(title,article) AGAINST('politics') INTO $id");
	   		echo $id;
	   		// the message
	   		// file_put_contents($log, $results, FILE_APPEND);
			$msg = "First line of text\nSecond line of text";

			// use wordwrap() if lines are longer than 70 characters
			$msg = wordwrap($msg,70);

			// send email
			mail("cmclaren89@gmail.com","My subject",$msg);
            // $sql =  "SELECT * FROM news WHERE MATCH(title,article) AGAINST('politics') LIMIT $first_pos, $RESULTS_LIMIT";
            // $sql_result_query = mysql_query($sql);         
        }
	   // else {
    //         $sql = "SELECT * FROM news WHERE (title LIKE '%".mysql_real_escape_string($search_term)."%' OR article LIKE '%".$search_term."%') ";
    //         $sql_query = mysql_query($sql);
    //         $results = mysql_num_rows($sql_query);
    //         $sql_result_query = mysql_query("SELECT * FROM news WHERE (title LIKE '%".$search_term."%' OR article LIKE '%".$search_term."%') LIMIT $first_pos, $RESULTS_LIMIT ");
    //     }
	   // $stop_search = getmicrotime();
	     //calculating the search time
	   // $time_search = ($stop_search - $start_search);

	   //----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		// }
		$run ++;
		// $run = false;
        sleep(5);
    }//end while
}//end if
 
?>

<?php
	// $user = "root";
	// $database = "search_1";
	// $hostname = "localhost";
	// $password = "RenVenrascal";
	// mysql_connect($hostname, $user, $password) or die ("Database connection failed.");
	// mysql_select_db($database) or die ("Database selection failed.");
	// echo "string";
	// if(isset($_GET['search']) && isset($_GET['submit'])) {
	//     $search_term = $_GET['search'];
	//     echo "success";
	// }

?>



<!-- retrieve keywords -->
<!-- query database -->
<!-- display result -->

<!-- retrieve keywords -->
<!-- <form>
	<fieldset>
		<legend>Search</legend>
		<input type="text" name="search" value="Type here...">
		<input type="submit" name="submit" value="Search">
	</fieldset>
</form> -->
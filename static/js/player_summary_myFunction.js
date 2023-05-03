function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("mytable1");
    tr = table.getElementsByTagName("tr");
    
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 2; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        console.log(td)
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
        }
    }

    table = document.getElementById("mytable2");
    tr = table.getElementsByTagName("tr");
    
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 2; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[1];
        if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
        }
    }

    }
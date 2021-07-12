function matt_edit_distance(string1,string2){
    m = string1.length
    n = string2.length
    d = []
    temp = []
    
    for (i = 0; i < n+1; i++){temp.push(0);}
    for (i = 0; i < m+1; i++){d.push(temp.slice());}
    for (i = 0; i < m+1; i++) {d[i][0] = i;}
    for (i = 0; i < n+1; i++) {d[0][i] = i;}

    for (j = 1; j < n+1; j++){
        for (i = 1; i < m+1; i++){
           if(string1[i-1] == string2[j-1]){
               d[i][j] = d[i-1][j-1]
           }
           else{
               d[i][j] = Math.min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1 )
           }
        }
    }

   return d[m][n]
}

function run(params) {

    //MUST HAVE PARAMETERS
    var nameCat = "cust_first_name"
    var idCat = "cust_acct_id";
    
    var space = params.space || "bac";
    var name = params.name || "burt";
    
    var theItem = nameCat + ":" + name.substring(0,name.length-1) + "*"
    
    
    var resultSize = 60;
    var results = [];
    var num_results = 0
    var similarItemsConnections=connections(space).q(theItem).ps(resultSize).c(idCat);
    var similarItems = similarItemsConnections.get();
    similarItems.r.forEach(function (r) {
        var namesConn = connections(space).q(r.a.c + ":" + r.a.v).ps(resultSize).c(nameCat);
        namesConn.get().r.forEach(function(r2) {
            results.push({"acct_id": r.a.v, "first_name" : r2.a.v, "edit_dist": matt_edit_distance(name,r2.a.v)});    
            num_results = num_results + 1
        })
        
    })
    results.push({"NUM RESULTS" : num_results})
    return results;
    //return JSON.stringify(table);
}

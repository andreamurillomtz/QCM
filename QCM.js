fetch("/Users/andreamurillo/Downloads/dataset1.txt")
    .then(function (res) {
        return res.text();
    })
    .then(function (data) {
        console.log(data);
    });

$(document).ready(function() {
    // Event listener for the search button
    $('#searchButton').click(function() {
        // Get the search term from the input field
        var searchTerm = $('#searchInput').val();
        
        // Make a GET request to your JSON file or API endpoint
        $.ajax({
            url: '../backend/my_list.json', // Replace 'your_api_endpoint_here' with the actual API endpoint
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                // Handle the successful response
                // Filter the data based on the search term
                var filteredData = data.filter(function(job) {
                    return job['Job title'].toLowerCase().includes(searchTerm.toLowerCase());
                });
                
                // Clear the existing job posts
                $('.post-list').empty();
                
                // Display the filtered job posts
                filteredData.forEach(function(job) {
                    var postHtml = `
                        <div class="single-post d-flex flex-row">
                            <div class="thumb">
                                <img src="img/post.png" alt="">
                            </div>
                            <div class="details">
                                <div class="title d-flex flex-row justify-content-between">
                                    <div class="titles">
                                        <a href="#"><h4>${job['Job title']}</h4></a>
                                        <h6>${job['Location']}</h6>
                                    </div>
                                    <ul class="btns">
                                        <li><a href="#"><span class="lnr lnr-heart"></span></a></li>
                                        <li><a href="#">Apply</a></li>
                                    </ul>
                                </div>
                                <p>${job['Description']}</p>
                                <h5>Job type: ${job['Job type']}</h5>
                                <p class="address">Salary: ${job['Salary']}</p>
                            </div>
                        </div>
                    `;
                    $('.post-list').append(postHtml);
                });
            },
            error: function(xhr, status, error) {
                // Handle errors
                console.error(error);
            }
        });
    });
});

<template>
     <span id="msg" class=" form-control alert" >
     </span>
    <form @submit.prevent="saveMovie" method="POST" id="movieForm" >
        <div class="form-group col-md-10">
            <label for="title">Movie Title</label>
            <input type="text" class="form-control" id="title" rows="1" name="title" />
        </div>
        
        <div class="form-group col-md-10">
            <label for="description">Description</label>
            <input type="text" class="form-control" id="description" rows="3" name="description" />
        </div>

        <div class="form-group col-md-5">
            <label for="photo">Poster Upload</label><br>
            <input type="file" class="form-control-file" id="poster"  name="poster" />
        </div>

        <div class="form-group" id="fbutton">
            <button type="submit" class="btn btn-primary col-md-2"> Save Movie </button>
        </div>
    </form>
</template>

<script setup>
    
        methods: {
            saveMovie(){
                fetch("/api/v1/movies", {
                    method: 'POST'
                })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (data) {
                        // display a success message
                        console.log(data);
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
        }
}
</script>
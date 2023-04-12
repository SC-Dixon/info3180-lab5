<template>
    
    <div class="container p-1">
        <h2>Movies</h2>
        <div class="row row-cols-2 g-4">  
            <div v-for="movie in movies" class="card-deck">
                <div class="card  w-100" Style="height: 100%">
                    <div class="row no-gutters">
                        <div class="col-md-4">
                            <img v-bind:src="movie.poster" class="card-imgs rounded-start">
                        </div>
                        <div class="col-md-7">
                            <div class="card-block px-2"> 
                                <h4 class="card-title pt-2">{{movie.title}} </h4>
                    
                                <p class="card-text">{{movie.description}}</p>
            
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
        
        </div>

    </div>
   
</template>


<script setup>
import { ref, onMounted } from "vue";
let movies = ref([]);

onMounted(() => {
    fetchMovies();
});

    function fetchMovies()
    {

        fetch("/api/v1/movies", {
        method: 'GET'
        })
        .then((response)=>{
            return response.json();
        })
        .then((data)=>{
            console.log(data);
            movies.value = data.movies
        })
        .catch((error)=>{
            console.log(error);
        })
    }
</script>

<style>
.card-imgs{
    height:250px;
    width: 180px;
}
</style>
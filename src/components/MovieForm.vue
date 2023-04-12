<template>
    <div v-if="errorMsg" class="alert alert-danger">
        <ul>
            <li v-for="error in errorMsg">{{ error }}</li>
        </ul>
    </div>

    <div v-if="successMsg" class="alert alert-success">{{ successMsg }}</div>

    <form @submit.prevent="saveMovie" method="POST" id="movieForm" >
        <div class="form-group col-md-7 pb-3">
            <label for="title">Movie Title<span class="text-danger"> (Required)</span></label>
            <input type="text" class="form-control" id="title"  name="title" />
        </div>
        
        <div class="form-group col-md-7 pb-3">
            <label for="description">Description <span class="text-danger">(Required)</span></label>
            <textarea  class="form-control" id="description" rows="5" name="description" v-model="text"></textarea>
        </div>

        <div class="form-group col-md-5 pb-3">
            <label for="photo">Poster Upload <span class="text-danger">(Required)</span></label><br>
            <input type="file" class="form-control" accept="image/png, image/jpeg, image/jpg" id="poster"  name="poster" />
        </div>

        <div class="form-group" id="fbutton">
            <button type="submit" class="btn btn-primary"> Save Movie </button>
        </div>
    </form>
</template>

<script setup>
import { ref, onMounted } from "vue";
let csrf_token = ref("");
let errorMsg = ref("");
let successMsg = ref("");

onMounted(() => {
 getCsrfToken();
});


    function saveMovie()
    {
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
        .then((response)=>{
            return response.json();
        })
        .then((data)=>{
            // display a success message
            console.log(data);
            if ("errors" in data){
                errorMsg.value = data.errors;
            } else {
                successMsg.value = data.message;
                resetFormFields();
            }
        })
        .catch((error)=>{
            console.log(error);
        });

        
    }

    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
    }

    function resetFormFields(){
    errorMsg.value = "";
    title.value = "";
    description.value = "";
    poster.value = "";
}
</script>




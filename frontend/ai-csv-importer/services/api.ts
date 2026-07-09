import axios from "axios";

const api =  axios.create({
    baseURL:"https://ai-csv-importer-project.onrender.com/api/",
});

export default api;


<template>
  

  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="student.name">
        <input type="text" class="form-control col-3 mx-2" placeholder="Course" v-model="student.course">
        <input type="text" class="form-control col-3 mx-2" placeholder="Rating" v-model="student.rating">
        <button type="submit" class="btn btn-info">Create</button>
      </div>
    </form>

    <table class="table table-striped table-dark">
      <thead>
        <tr>
          <th scope="col">Name</th>
          <th scope="col">Course</th>
          <th scope="col">Rating</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @click="$data.student = student">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td>
            <button class="btn btn-danger btn-sm mx-1" @click="deleteStudent(student)">X</button>
          </td>
        </tr>
      </tbody>
    </table>   
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      student: {},
      students: []
    }
  },

  async created(){
    await this.getStudents();
  },

  methods: {

    submitForm(){
      if (this.student.id === undefined) {
          this.createStudent();
      } else {
          this.editStudent();
      }
    },

    async getStudents(){
      var response = await fetch('http://localhost:8000/api/students/');
      this.students = await response.json();
    },

    async createStudent(){
      await this.getStudents();

      await fetch('http://localhost:8000/api/students/',{
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.student)
      });
      // this.students.push(await response.json())
      await this.getStudents();
      this.student = {};
    },

    async editStudent(){
      await this.getStudents();

      await fetch(`http://localhost:8000/api/students/${this.student.id}/`,{
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.student)
      });
      // this.students.push(await response.json())
      await this.getStudents();
      this.student = {};
    },

    async deleteStudent(student){
      await this.getStudents();

      await fetch(`http://localhost:8000/api/students/${student.id}/`,{
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this.student)
      });
      // this.students.push(await response.json())
      await this.getStudents();
      this.student = {};
    }

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

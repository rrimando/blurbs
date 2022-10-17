<template>
  <b-container class="blurb_container">
    <b-row>
      <b-col class="offset-1">
        <div class="add_blurb">
          <b-form v-on:submit.prevent="submitForm">
            <h1>Blurb</h1>
            <b-row>
              <b-col cols="3">
                <b-form-group>
                  <b-form-input
                    id="name"
                    v-model="name"
                    placeholder="Name"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col cols="6">
                <b-form-group>
                  <b-form-textarea
                    id="blurb"
                    v-model="blurb"
                    placeholder="What's on your mind? ..."
                    :maxLength="blurbMaxLength"
                  >
                  </b-form-textarea>
                  <span
                    >{{ blurbMaxLength - blurb.length }} /
                    {{ blurbMaxLength }}</span
                  >
                </b-form-group>
              </b-col>
              <b-col cols="3">
                <b-form-group>
                  <b-button type="submit">Blurb it! &raquo;</b-button>
                </b-form-group>
              </b-col>
            </b-row>
          </b-form>
        </div>
        <hr />
        <div class="blurb_content">
          <h1>Blurbs</h1>
          <b-table striped hover :items="blurbs" :fields="fields"></b-table>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: "BlurbsComponent",
  data() {
    return {
      blurbMaxLength: 50,
      blurb: "",
      blurbs: [],
      name: "",
      fields: [
        {
          key: "name",
          sortable: true,
        },
        {
          key: "created_at",
          sortable: true,
        },
        {
          key: "blurb",
          sortable: false,
        },
      ],
    };
  },
  methods: {
    async getData() {
      try {
        // fetch blurbs
        const response = await this.$http.get(
          "http://localhost:8000/api/blurbs/"
        );
        // set the data returned as blurbs
        this.blurbs = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async submitForm() {
      try {
        // Send a POST request to the API
        const response = await this.$http.post(
          "http://localhost:8000/api/blurbs/",
          {
            name: this.name,
            blurb: this.blurb,
          }
        );
        // Append the returned data to the blurbs array
        this.blurbs.push(response.data);
        // Reset blurb field values.
        this.blurb = "";
      } catch (error) {
        // Log the error
        console.log(error);
      }
    },
    async toggleBlurb(blurb) {
      try {
        // Send a request to API to update the blurbs
        const response = await this.$http.put(
          `http://localhost:8000/api/blurbs/${blurb.id}/`,
          {
            published: !blurb.published,
            blurb: blurb.blurb,
          }
        );

        // Get the index of the task being updated
        let blurbIndex = this.blurbs.findIndex((b) => b.id === blurb.id);

        // Reset the blurbs array with the new data of the updated blurb

        this.blurbs = this.blurbs.map((blurb) => {
          if (this.blurbs.findIndex((b) => b.id === blurb.id) === blurbIndex) {
            return response.data;
          }
          return blurb;
        });
      } catch (error) {
        // Log any error
        console.log(error);
      }
    },
    async deleteBlurb(blurb) {
      // Confirm if one wants to delete the blurb
      let confirmation = confirm("Do you want to delete this blurb?");

      if (confirmation) {
        try {
          // Send a request to delete the blurb
          await this.$http.delete(
            `http://localhost:8000/api/blurbs/${blurb.id}`
          );

          // Refresh the blurbs
          this.getData();
        } catch (error) {
          // Log any error

          console.log(error);
        }
      }
    },
  },
  created() {
    // Fetch blurbs on page load
    this.getData();
  },
};
</script>

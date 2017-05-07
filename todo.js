import Ember from 'ember';

export default DS.Model.extend({
  name: DS.attr('string'),
  degree: DS.attr('string'),
  title: Ember.computed.alias('degree'),

  fullName: Ember.computed('name', 'degree', function() {
    return `${this.get('degree')} ${this.get('name')}`;
  }),

  derpy: Ember.computed(function() {
    return this.derp;
  })
});
